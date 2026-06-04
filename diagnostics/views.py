from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .inference import AIProcessor
from encyclopedia.models import Disease
from django.contrib.auth.decorators import login_required
from .models import DiagnosticReport, GuestIPLimit
from django.shortcuts import get_object_or_404, redirect
import datetime

ai_engine = AIProcessor()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def diagnose_view(request):
    context = {}

    # Token limit check for guest/unauthenticated users
    if not request.user.is_authenticated:
        ip = get_client_ip(request)
        today = datetime.date.today()
        
        # Get or create daily IP limit record
        ip_limit, created = GuestIPLimit.objects.get_or_create(
            ip_address=ip,
            date=today,
            defaults={'tokens': 50}
        )
        guest_tokens = ip_limit.tokens
        context['guest_tokens'] = guest_tokens
    else:
        context['guest_tokens'] = 50  # Dummy for template if needed

    if request.method == 'POST':
        if not request.user.is_authenticated:
            if guest_tokens < 25:
                context['token_error'] = True
                return render(request, 'diagnostics/diagnose.html', context)

        if request.FILES.get('leaf_image'):
            uploaded_file = request.FILES['leaf_image']
            model_choice = request.POST.get('model_choice', 'custom_cnn')  # Dropdown'dan gelen model adı

            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)
            original_url = fs.url(filename)

            # inference.py'den 3 görselin de URL'sini alıyoruz
            class_id, confidence, nobg_url, heatmap_url = ai_engine.process(file_path, model_choice)

            disease = Disease.objects.filter(ai_class_id=class_id).first()
            context['disease'] = disease

            # Deduct tokens for guest if successful
            if not request.user.is_authenticated:
                guest_tokens = max(0, guest_tokens - 25)
                ip_limit.tokens = guest_tokens
                ip_limit.save()
                context['guest_tokens'] = guest_tokens

            # Analiz sonucunu veritabanına kaydetme işlemi
            if request.user.is_authenticated:
                # Çiftçi profilini bul
                farmer_profile = request.user.profile # FarmerProfile modeli User'a 'profile' adıyla bağlı
                report = DiagnosticReport.objects.create(
                    farmer=farmer_profile,
                    original_image=uploaded_file,
                    detected_disease=disease,
                    confidence_score=confidence
                )
                if heatmap_url:
                    heatmap_filename = heatmap_url.replace('/media/', '') # Filename relative to media root
                    report.heatmap_image = heatmap_filename
                    report.save()

            context.update({
                'confidence': round(confidence, 1),
                'original_image': original_url,
                'nobg_image': nobg_url,
                'heatmap_image': heatmap_url,
                'selected_model': model_choice,
                'result_ready': True
            })

    return render(request, 'diagnostics/diagnose.html', context)

@login_required
def diagnostic_history_view(request):
    # Kullanıcının kendi raporlarını en yeniden en eskiye doğru çekiyoruz
    reports = DiagnosticReport.objects.filter(farmer__user=request.user).order_by('-created_at')
    return render(request, 'diagnostics/history.html', {'reports': reports})


@login_required
def diagnostic_detail_view(request, pk):
    # Kullanıcı SADECE kendi raporunu görebilir (Güvenlik)
    report = get_object_or_404(DiagnosticReport, pk=pk, farmer__user=request.user)
    return render(request, 'diagnostics/diagnostic_detail.html', {'report': report})


@login_required
def delete_diagnostic_view(request, pk):
    # Kullanıcı SADECE kendi raporunu silebilir (Güvenlik)
    report = get_object_or_404(DiagnosticReport, pk=pk, farmer__user=request.user)

    if request.method == 'POST':
        report.delete()

    return redirect('diagnostic_history')