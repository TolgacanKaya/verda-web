from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .inference import AIProcessor
from encyclopedia.models import Disease
from accounts.models import FarmerProfile
from django.contrib.auth.models import User
from .models import DiagnosticReport, GuestIPLimit
import datetime

ai_engine = AIProcessor()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def diagnose_api(request):
    """
    Mobil uygulamadan gelen fotoğrafı alır, modeli çalıştırır ve JSON döner.
    Kayıtsız misafirler için IP tabanlı günlük token kontrolü ve düşümü gerçekleştirir.
    Kayıtlı kullanıcılar için veritabanında DiagnosticReport oluşturur.
    """
    username = request.GET.get('username') or request.POST.get('username')
    is_guest = (username == 'Misafir' or not username)

    # 1. IP tabanlı misafir limit kontrolü
    ip_limit = None
    if is_guest:
        ip = get_client_ip(request)
        today = datetime.date.today()
        ip_limit, _ = GuestIPLimit.objects.get_or_create(
            ip_address=ip,
            date=today,
            defaults={'tokens': 50}
        )

    # GET isteğinde sadece kalan token miktarını dönüyoruz
    if request.method == 'GET':
        if is_guest:
            return JsonResponse({
                'status': 'success',
                'guest_tokens': ip_limit.tokens,
                'is_logged_in': False
            })
        else:
            return JsonResponse({
                'status': 'success',
                'guest_tokens': 50,
                'is_logged_in': True
            })

    if request.method == 'POST':
        # Misafir kullanıcının yeterli tokenı var mı kontrol et
        if is_guest:
            if ip_limit.tokens < 25:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Günlük limitinize ulaştınız. Sınırsız teşhis için lütfen üye olun!',
                    'token_error': True,
                    'guest_tokens': ip_limit.tokens
                }, status=400)

        if request.FILES.get('leaf_image'):
            uploaded_file = request.FILES['leaf_image']
            model_choice = request.POST.get('model_choice', 'custom_cnn')

            # Görseli geçici olarak media klasörüne kaydet
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)
            original_url = fs.url(filename)

            try:
                # inference.py üzerinden yapay zekayı çalıştır
                class_id, confidence, nobg_url, heatmap_url = ai_engine.process(file_path, model_choice)

                # Veritabanından hastalığı bul
                disease = Disease.objects.filter(ai_class_id=class_id).first()
                if disease:
                    disease_name = disease.name
                    treatment = disease.chemical_treatment
                else:
                    disease_name = "Bilinmeyen Hastalık"
                    treatment = "Veritabanında çözüm bulunamadı."

                # Token düşme işlemi (Misafir ise)
                guest_tokens = 50
                if is_guest:
                    ip_limit.tokens = max(0, ip_limit.tokens - 25)
                    ip_limit.save()
                    guest_tokens = ip_limit.tokens

                # Kayıtlı kullanıcı ise teşhis raporunu kaydet
                if not is_guest and username:
                    profile = FarmerProfile.objects.filter(user__username=username).first()
                    if profile:
                        report = DiagnosticReport.objects.create(
                            farmer=profile,
                            original_image=filename,
                            detected_disease=disease,
                            confidence_score=confidence
                        )
                        if heatmap_url:
                            heatmap_filename = heatmap_url.replace(settings.MEDIA_URL, '')
                            report.heatmap_image = heatmap_filename
                            report.save()

                # Başarılı JSON yanıtı
                return JsonResponse({
                    'status': 'success',
                    'disease': disease_name,
                    'confidence': round(confidence, 1),
                    'treatment': treatment,
                    'original_image': request.build_absolute_uri(original_url),
                    'nobg_image': request.build_absolute_uri(nobg_url),
                    'heatmap_image': request.build_absolute_uri(heatmap_url),
                    'guest_tokens': guest_tokens,
                    'is_logged_in': not is_guest
                })
                
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request or no image provided.'}, status=400)

@csrf_exempt
def delete_diagnostic_api(request, pk):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            return JsonResponse({'status': 'error', 'message': 'Kullanıcı adı gerekli.'}, status=400)
        
        try:
            report = DiagnosticReport.objects.get(pk=pk)
            # Yalnızca raporun sahibi silebilir
            if report.farmer.user.username == username:
                report.delete()
                return JsonResponse({'status': 'success', 'message': 'Teşhis başarıyla silindi.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Yetkisiz erişim.'}, status=403)
        except DiagnosticReport.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Teşhis bulunamadı.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Sadece POST desteklenir.'}, status=405)

