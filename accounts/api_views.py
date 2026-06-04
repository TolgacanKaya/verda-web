from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FarmerProfile
from django.contrib.auth.models import User
from diagnostics.models import DiagnosticReport

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
def get_profile_api(request):
    """Mobil uygulama için çiftçi profili verilerini döner ve günceller."""
    if request.method == 'GET':
        username = request.GET.get('username')
        if username:
            profile = FarmerProfile.objects.filter(user__username=username).first()
        else:
            profile = FarmerProfile.objects.first()
        
        if not profile:
            # Eğer DB boşsa geçici profil oluştur
            target_username = username or 'mobil_kullanici'
            user, _ = User.objects.get_or_create(username=target_username, defaults={'email': f'{target_username}@alziraat.com'})
            profile, _ = FarmerProfile.objects.get_or_create(user=user, defaults={'location': 'Mobil Şehir'})
            
        data = {
            'username': profile.user.username,
            'first_name': profile.user.first_name,
            'last_name': profile.user.last_name,
            'email': profile.user.email,
            'role': 'Uzman Çiftçi', # Sabit örnek değer
            'location': profile.location or 'Belirtilmemiş',
            'bio': profile.bio or 'Henüz biyografi eklenmemiş.',
            'profile_picture': request.build_absolute_uri(profile.profile_picture.url) if profile.profile_picture else "",
            'cover_picture': request.build_absolute_uri(profile.cover_picture.url) if profile.cover_picture else "",
            'grown_plants': [],
            'favorite_plants': [],
            'diagnoses': []
        }
        
        for plant in profile.grown_plants.all():
            data['grown_plants'].append({
                'id': plant.id,
                'name': plant.name,
                'image': request.build_absolute_uri(plant.image.url) if plant.image else ""
            })
            
        for plant in profile.favorite_plants.all():
            data['favorite_plants'].append({
                'id': plant.id,
                'name': plant.name,
                'image': request.build_absolute_uri(plant.image.url) if plant.image else ""
            })
            
        # Teşhis geçmişi (Grad-CAM görseli, güven skoru vb. ile)
        for report in profile.reports.select_related('detected_disease').all().order_by('-created_at'):
            disease = report.detected_disease
            data['diagnoses'].append({
                'id': report.id,
                'disease_name': disease.name if disease else "Bilinmeyen Hastalık",
                'confidence_score': report.confidence_score,
                'original_image': request.build_absolute_uri(report.original_image.url) if report.original_image else "",
                'heatmap_image': request.build_absolute_uri(report.heatmap_image.url) if report.heatmap_image else "",
                'is_user_verified': report.is_user_verified,
                'created_at': format_date_tr(report.created_at),
                'symptoms': disease.symptoms if disease else "Belirti bilgisi bulunmuyor.",
                'organic_treatment': disease.organic_treatment if disease else "Organik çözüm tavsiyesi bulunmuyor.",
                'chemical_treatment': disease.chemical_treatment if disease else "Kimyasal çözüm tavsiyesi bulunmuyor.",
                'prevention': disease.prevention if disease else "Önleyici tedbir tavsiyesi bulunmuyor."
            })
            
        return JsonResponse({'status': 'success', 'data': data})
        
    elif request.method == 'POST':
        # Profil güncelleme işlemi
        username = request.GET.get('username') or request.POST.get('username')
        if not username:
            import json
            try:
                data = json.loads(request.body)
                username = data.get('username')
            except:
                pass
                
        if not username:
            return JsonResponse({'status': 'error', 'message': 'Kullanıcı adı gereklidir.'}, status=400)
            
        profile = FarmerProfile.objects.filter(user__username=username).first()
        if not profile:
            return JsonResponse({'status': 'error', 'message': 'Profil bulunamadı.'}, status=404)
            
        location = None
        bio = None
        first_name = None
        last_name = None
        email = None
        profile_pic_base64 = None
        cover_pic_base64 = None
        grown_plants_ids = None
        
        if request.content_type == 'application/json':
            import json
            try:
                data = json.loads(request.body)
                location = data.get('location')
                bio = data.get('bio')
                first_name = data.get('first_name')
                last_name = data.get('last_name')
                email = data.get('email')
                profile_pic_base64 = data.get('profile_picture')
                cover_pic_base64 = data.get('cover_picture')
                grown_plants_ids = data.get('grown_plants')
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Geçersiz JSON: {str(e)}'}, status=400)
        else:
            location = request.POST.get('location')
            bio = request.POST.get('bio')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            if 'cover_picture' in request.FILES:
                profile.cover_picture = request.FILES['cover_picture']
            grown_plants_ids = request.POST.getlist('grown_plants') or request.POST.get('grown_plants')
            if isinstance(grown_plants_ids, str):
                try:
                    grown_plants_ids = [int(x.strip()) for x in grown_plants_ids.split(',') if x.strip()]
                except:
                    grown_plants_ids = None
                
        user = profile.user
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if email is not None:
            user.email = email
        user.save()
        
        if location is not None:
            profile.location = location
        if bio is not None:
            profile.bio = bio
        if grown_plants_ids is not None:
            profile.grown_plants.set(grown_plants_ids)
            
        if profile_pic_base64:
            import base64
            from django.core.files.base import ContentFile
            try:
                if 'data:image' in profile_pic_base64:
                    header, profile_pic_base64 = profile_pic_base64.split(';base64,')
                decoded_file = base64.b64decode(profile_pic_base64)
                profile.profile_picture.save(f'{username}_profile.jpg', ContentFile(decoded_file), save=False)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Görsel çözümlenemedi: {str(e)}'}, status=400)
                
        if cover_pic_base64:
            import base64
            from django.core.files.base import ContentFile
            try:
                if 'data:image' in cover_pic_base64:
                    header, cover_pic_base64 = cover_pic_base64.split(';base64,')
                decoded_file = base64.b64decode(cover_pic_base64)
                profile.cover_picture.save(f'{username}_cover.jpg', ContentFile(decoded_file), save=False)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'Kapak görseli çözümlenemedi: {str(e)}'}, status=400)
                
        profile.save()
        return JsonResponse({'status': 'success', 'message': 'Profil başarıyla güncellendi.'})
        
    return JsonResponse({'status': 'error', 'message': 'Invalid method.'}, status=405)

@csrf_exempt
def api_login(request):
    """Mobil uygulama için giriş yapma ucu."""
    if request.method == 'POST':
        import json
        from django.contrib.auth import authenticate
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Gerçekte Token dönmeli, geliştirme için dummy token
                return JsonResponse({'status': 'success', 'token': 'dummy_token_123', 'username': user.username})
            return JsonResponse({'status': 'error', 'message': 'Kullanıcı adı veya şifre hatalı.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)

@csrf_exempt
def api_register(request):
    """Mobil uygulama için kayıt olma ucu."""
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'error', 'message': 'Bu kullanıcı adı zaten alınmış.'}, status=400)
            user = User.objects.create_user(username=username, email=f"{username}@alziraat.com", password=password)
            FarmerProfile.objects.create(user=user, location="Mobil Uygulama")
            return JsonResponse({'status': 'success', 'message': 'Kayıt başarılı! Giriş yapabilirsiniz.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)


@csrf_exempt
def toggle_favorite_api(request):
    """Favori bitki ekleme/çıkarma işlemi."""
    if request.method == 'POST':
        import json
        username = None
        plant_id = None
        
        try:
            data = json.loads(request.body)
            username = data.get('username')
            plant_id = data.get('plant_id')
        except:
            # Fallback for standard form posts
            plant_id = request.POST.get('plant_id')

        # Fallback to session user if authenticated
        if not username and request.user.is_authenticated:
            username = request.user.username
            
        if not username or not plant_id:
            return JsonResponse({'status': 'error', 'message': 'Eksik parametre.'}, status=400)
            
        profile = FarmerProfile.objects.filter(user__username=username).first()
        if not profile:
            return JsonResponse({'status': 'error', 'message': 'Profil bulunamadı.'}, status=404)
            
        from encyclopedia.models import Plant
        plant = Plant.objects.filter(id=plant_id).first()
        if not plant:
            return JsonResponse({'status': 'error', 'message': 'Bitki bulunamadı.'}, status=404)
            
        if plant in profile.favorite_plants.all():
            profile.favorite_plants.remove(plant)
            is_favorite = False
            msg = "Bitki favorilerden çıkarıldı."
        else:
            profile.favorite_plants.add(plant)
            is_favorite = True
            msg = "Bitki favorilere eklendi."
            
        return JsonResponse({'status': 'success', 'is_favorite': is_favorite, 'message': msg})
        
    return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)


@csrf_exempt
def favorite_plants_ai_api(request):
    """Favoriye alınan bitkilere özel Gemini AI ziraat tavsiyesi ve rehber üretimi."""
    if request.method == 'POST':
        import json
        username = None
        try:
            data = json.loads(request.body)
            username = data.get('username')
        except:
            pass
            
        # Fallback to session user if authenticated
        if not username and request.user.is_authenticated:
            username = request.user.username
            
        if not username:
            return JsonResponse({'status': 'error', 'message': 'Eksik parametre.'}, status=400)
            
        profile = FarmerProfile.objects.filter(user__username=username).first()
        if not profile:
            return JsonResponse({'status': 'error', 'message': 'Profil bulunamadı.'}, status=404)
            
        favorites = profile.favorite_plants.all()
        if not favorites:
            return JsonResponse({
                'status': 'success', 
                'answer': 'Henüz favori bitki eklememişsiniz. Ansiklopedi sayfasından bitki favorileyerek buraya özel AI ziraat rehberinizi oluşturabilirsiniz!'
            })
            
        plant_names = ", ".join([p.name for p in favorites])
        
        import google.generativeai as genai
        try:
            genai.configure(api_key="AIzaSyBOWZwCsSc4yGJjuf3zLSbEugxdUA9k1Ws")
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            prompt = (
                f"Sen tecrübeli bir kıdemli ziraat mühendisliği yapay zeka asistanısın. "
                f"Çiftçimiz tarlasında veya bahçesinde şu bitkileri favorilerine ekledi ve yetiştiriyor/yetiştirmek istiyor: {plant_names}. "
                f"Bu bitki kombinasyonuna göre çiftçimize özel, son derece yararlı ve premium bir zirai tavsiye raporu yaz. "
                f"İçerik şunları barındırsın:\n"
                f"1. Ortak sulama uyumu ve nem dengesi tavsiyeleri,\n"
                f"2. Gübreleme ve toprak besin gereksinimleri (ortak paydalar),\n"
                f"3. Bu bitkilerin yan yana dikilmesi durumunda birbirini olumlu etkileyip etkilemeyeceği (kardeş bitki uyumu),\n"
                f"4. Mevsimlik kritik bakım önerileri.\n\n"
                f"Lütfen samimi, teşvik edici, net, anlaşılır ve madde madde yanıt ver."
            )
            
            response = model.generate_content(prompt)
            return JsonResponse({'status': 'success', 'answer': response.text})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Gemini hatası: {str(e)}'}, status=500)
            
    return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)

