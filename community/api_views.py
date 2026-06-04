import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .models import Post, Comment
from accounts.models import FarmerProfile
from django.contrib.auth.models import User

def format_date_tr(dt):
    if not dt:
        return ""
    months_tr = {
        'Jan': 'Oca', 'Feb': 'Şub', 'Mar': 'Mar', 'Apr': 'Nis',
        'May': 'May', 'Jun': 'Haz', 'Jul': 'Tem', 'Aug': 'Ağu',
        'Sep': 'Eyl', 'Oct': 'Eki', 'Nov': 'Kas', 'Dec': 'Ara'
    }
    date_str = dt.strftime('%d %b %Y, %H:%M')
    for eng, tr in months_tr.items():
        if eng in date_str:
            date_str = date_str.replace(eng, tr)
            break
    return date_str

@csrf_exempt
def community_api(request):
    """Köy Meydanı gönderilerini getirir veya yeni gönderi oluşturur."""
    if request.method == 'GET':
        posts = Post.objects.select_related('author__user', 'related_plant').prefetch_related('comments__author__user', 'comments__replies__author__user').all()
        data = []
        for post in posts:
            post_data = {
                'id': post.id,
                'author': post.author.user.username,
                'author_role': 'Kayıtlı Çiftçi',
                'author_avatar': request.build_absolute_uri(post.author.profile_picture.url) if post.author.profile_picture else "",
                'content': post.content,
                'image': request.build_absolute_uri(post.image.url) if post.image else "",
                'related_plant': post.related_plant.name if post.related_plant else None,
                'is_solved': post.is_solved,
                'created_at': format_date_tr(post.created_at),
                'comments': []
            }
            # Sadece üst düzey (parent=None) yorumları filtreleyip dönüyoruz
            for comment in post.comments.filter(parent=None):
                comment_dict = {
                    'id': comment.id,
                    'author': comment.author.user.username,
                    'author_avatar': request.build_absolute_uri(comment.author.profile_picture.url) if comment.author.profile_picture else "",
                    'content': comment.content,
                    'is_expert_advice': comment.is_expert_advice,
                    'created_at': format_date_tr(comment.created_at),
                    'replies': []
                }
                # Bu yoruma atılan yanıtları ekliyoruz
                for reply in comment.replies.all():
                    comment_dict['replies'].append({
                        'id': reply.id,
                        'author': reply.author.user.username,
                        'author_avatar': request.build_absolute_uri(reply.author.profile_picture.url) if reply.author.profile_picture else "",
                        'content': reply.content,
                        'is_expert_advice': reply.is_expert_advice,
                        'created_at': format_date_tr(reply.created_at)
                    })
                post_data['comments'].append(comment_dict)
            data.append(post_data)
        return JsonResponse({'status': 'success', 'data': data})
        
    elif request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if not content:
            return JsonResponse({'status': 'error', 'message': 'İçerik alanı zorunludur.'}, status=400)
            
        try:
            username = request.POST.get('username')
            author = None
            if username:
                author = FarmerProfile.objects.filter(user__username=username).first()
            if not author:
                author = FarmerProfile.objects.first()
            if not author:
                # Çiftçi profili yoksa otomatik oluştur
                target_username = username or 'mobil_kullanici'
                user, _ = User.objects.get_or_create(username=target_username, defaults={'email':f'{target_username}@alziraat.com'})
                user.set_password('mobil123')
                user.save()
                author, _ = FarmerProfile.objects.get_or_create(user=user, defaults={'location':'Mobil Uygulama'})
                
            post = Post.objects.create(
                author=author,
                content=content,
                image=image
            )
            return JsonResponse({'status': 'success', 'message': 'Gönderi paylaşıldı!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)

@csrf_exempt
def comment_api(request):
    """Mobil uygulama için gönderiye veya yoruma yanıt ekleme ucu."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post_id = data.get('post_id')
            content = data.get('content')
            username = data.get('username')
            parent_id = data.get('parent_id')
            
            post = Post.objects.get(id=post_id)
            author = None
            if username:
                author = FarmerProfile.objects.filter(user__username=username).first()
            if not author:
                author = FarmerProfile.objects.first()
            if not author:
                target_username = username or 'mobil_kullanici'
                user, _ = User.objects.get_or_create(username=target_username, defaults={'email':f'{target_username}@alziraat.com'})
                author, _ = FarmerProfile.objects.get_or_create(user=user, defaults={'location':'Mobil Uygulama'})
                
            parent = None
            if parent_id:
                parent = Comment.objects.filter(id=parent_id).first()
                
            comment = Comment.objects.create(
                post=post,
                parent=parent,
                author=author,
                content=content,
                is_expert_advice=author.user.is_staff
            )
            return JsonResponse({
                'status': 'success',
                'message': 'Yorum eklendi!',
                'comment': {
                    'id': comment.id,
                    'author': comment.author.user.username,
                    'author_avatar': request.build_absolute_uri(comment.author.profile_picture.url) if comment.author.profile_picture else "",
                    'content': comment.content,
                    'is_expert_advice': comment.is_expert_advice,
                    'created_at': format_date_tr(comment.created_at),
                    'replies': []
                }
            })
        except Post.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Gönderi bulunamadı.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)

