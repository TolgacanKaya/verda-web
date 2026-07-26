from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from diagnostics.models import DiagnosticReport
from accounts.models import FarmerProfile
from encyclopedia.models import Plant
from django.db.models import Count

def dashboard_view(request):
    context = {}

    # 1. PLATFORM GENELİ GERÇEK İSTATİSTİKLER (Herkes Görebilir)
    total_platform_scans = DiagnosticReport.objects.count()
    total_farmers = FarmerProfile.objects.count()

    # Platformda en çok rastlanan (Sağlıklı dışındaki) hastalık
    platform_top_disease = DiagnosticReport.objects.exclude(detected_disease__name__icontains="Sağlıklı") \
        .values('detected_disease__name') \
        .annotate(count=Count('detected_disease')) \
        .order_by('-count').first()

    # Dynamic featured plants for encyclopedia exploration hub
    featured_plants = Plant.objects.all()[:4]

    context.update({
        'total_platform_scans': total_platform_scans,
        'total_farmers': total_farmers,
        'platform_top_disease': platform_top_disease[
            'detected_disease__name'] if platform_top_disease else "Veri Bekleniyor",
        'featured_plants': featured_plants,
    })

    # 2. KULLANICIYA ÖZEL İSTATİSTİKLER (Sadece Giriş Yapanlar)
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        if profile:
            context['total_diagnostics'] = DiagnosticReport.objects.filter(farmer=profile).count()

            most_common = DiagnosticReport.objects.filter(farmer=profile) \
                .exclude(detected_disease__name__icontains="Sağlıklı") \
                .values('detected_disease__name') \
                .annotate(count=Count('detected_disease')) \
                .order_by('-count').first()

            context['most_common_disease'] = most_common['detected_disease__name'] if most_common else "Teşhis Yok"

    return render(request, 'core/home.html', context)
def about_view(request):
    return render(request, 'core/about.html')


def terms_view(request):
    return render(request, 'core/terms.html')

def privacy_view(request):
    return render(request, 'core/privacy.html')


def contact_view(request):
    return render(request, 'core/contact.html')




