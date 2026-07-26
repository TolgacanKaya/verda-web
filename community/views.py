from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Notification
from .forms import PostForm, CommentForm
from accounts.models import FarmerProfile
from django.http import JsonResponse
from django.utils.timesince import timesince
import json


ZIRAAT_TIPS = [
    "Erken yanıklığı önlemek için sabah erken saatlerde damlama sulama yapın. Yaprakların ıslak kalması mantar hastalıklarını tetikler.",
    "Tarlanızdaki yabancı otlarla mücadele etmek, kültür bitkilerinizin besin ve su rekabetini azaltarak verimi %20'ye kadar artırır.",
    "Potasyum oranı yüksek gübreler, bitkilerinizin kuraklığa ve soğuk hava şartlarına karşı direncini artıracaktır.",
    "Kalsiyum eksikliği domateslerde dip çürüklüğüne (çiçek burnu çürüklüğü) sebep olur. Sulama düzenine dikkat edin.",
    "Böcek zararlılarını uzak tutmak için kadife çiçeği gibi faydalı bitkileri tarlanızın sınırlarına ekebilirsiniz.",
    "Mantar hastalıklarının yayılmasını önlemek için budama makaslarınızı her kullanımdan sonra alkolle sterilize edin.",
    "Toprak analizini yaptırmadan gübreleme yapmayın. Aşırı azotlu gübreleme bitkileri hastalıklara daha duyarlı hale getirebilir.",
    "Uğur böcekleri gibi faydalı böcekleri tarlanıza çekmek için kimyasal ilaç kullanımını azaltın; yaprak bitlerini doğal yolla yok ederler.",
    "Hastalık belirtisi gösteren yaprak ve dalları budayıp tarladan uzaklaştırarak imha edin.",
    "Bitkilerinizin güçlü bir kök yapısına sahip olması için gelişim döneminin başında fosfor ağırlıklı gübrelemeyi tercih edin."
]

# @login_required SİLİNDİ
def feed_view(request):
    posts = Post.objects.select_related('author__user', 'related_plant').prefetch_related('comments').all()

    form = PostForm()
    # Sadece giriş yapmış kullanıcılar POST (yeni gönderi) atabilsin
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            farmer_profile, created = FarmerProfile.objects.get_or_create(user=request.user)
            post.author = farmer_profile
            post.save()
            return redirect('feed')

    # Köy Meydanı Yan Panelleri İçin İstatistikler ve Popüler Etiketler
    from django.db.models import Count
    from encyclopedia.models import Plant
    
    popular_plants = Plant.objects.annotate(post_count=Count('post')).filter(post_count__gt=0).order_by('-post_count')[:5]
    if not popular_plants.exists():
        # Fallback to general plants if no posts have tags yet
        popular_plants = Plant.objects.all()[:5]
        
    total_farmers = FarmerProfile.objects.count()
    total_posts = posts.count()
    solved_posts = Post.objects.filter(is_solved=True).count()

    import datetime
    day_of_year = datetime.date.today().timetuple().tm_yday
    tip_of_the_day = ZIRAAT_TIPS[day_of_year % len(ZIRAAT_TIPS)]

    context = {
        'posts': posts, 
        'form': form,
        'popular_plants': popular_plants,
        'total_farmers': total_farmers,
        'total_posts': total_posts,
        'solved_posts': solved_posts,
        'tip_of_the_day': tip_of_the_day
    }

    return render(request, 'community/feed.html', context)

@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Sadece ana yorumları çekiyoruz (parent=None)
    comments = post.comments.filter(parent=None).select_related('author__user').all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            
            # Eğer bir yoruma yanıt ise, parent_id'yi alıp bağla
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)

            farmer_profile, created = FarmerProfile.objects.get_or_create(user=request.user)
            comment.author = farmer_profile

            if request.user.is_superuser:
                comment.is_expert_advice = True
            comment.save()

            if post.author != comment.author:
                Notification.objects.create(
                    recipient=post.author,
                    sender=comment.author,
                    post=post,
                    text="gönderinize yorum yaptı."  # Şablonu sadeleştirdim, HTML'de isimle birleşecek
                )

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'community/post_detail.html', {'post': post, 'comments': comments, 'form': form})


# --- YENİ EKLENEN BİLDİRİM LİSTELEME VIEW ---
@login_required
def notifications_view(request):
    farmer_profile = request.user.profile
    notifications = Notification.objects.filter(recipient=farmer_profile).order_by('-created_at')

    # Sayfa açıldığı an tümünü okundu işaretle (kırmızı balon sönsün diye)
    notifications.filter(is_read=False).update(is_read=True)

    return render(request, 'community/notifications.html', {'notifications': notifications})

@login_required
def get_notifications_api(request):
    profile = getattr(request.user, 'profile', None)
    if not profile:
        return JsonResponse({'count': 0, 'notifications': []})

    notifs = Notification.objects.filter(recipient=profile).order_by('-created_at')[:5]
    count = Notification.objects.filter(recipient=profile, is_read=False).count()

    data = []
    for n in notifs:
        data.append({
            'id': n.id,
            # İŞTE BURASI DÜZELDİ: Artık yorum yapanın ismi ve metin birleşiyor
            'text': f"👤 {n.sender.user.username} {n.text}",
            'is_read': n.is_read,
            'time': f"{timesince(n.created_at)} önce",
            'url': f"/meydan/gonderi/{n.post.id}/"
        })

    return JsonResponse({'count': count, 'notifications': data})

@login_required
def mark_all_read_api(request):
    """Tüm bildirimleri okundu olarak işaretler"""
    if request.method == "POST":
        profile = getattr(request.user, 'profile', None)
        if profile:
            Notification.objects.filter(recipient=profile, is_read=False).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def delete_post_view(request, pk):
    """Köy Meydanı gönderisini siler"""
    post = get_object_or_404(Post, pk=pk)
    if post.author.user == request.user or request.user.is_superuser:
        post.delete()
    return redirect('feed')