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

def tarla_rehberi_view(request):
    from .models import FieldGuideItem
    items = FieldGuideItem.objects.all()
    context = {
        'ilkbahar_items': items.filter(season='İlkbahar'),
        'yaz_items': items.filter(season='Yaz'),
        'sonbahar_items': items.filter(season='Sonbahar'),
        'kis_items': items.filter(season='Kış'),
        'uretim_modelleri': items.filter(season='Genel'),
    }
    return render(request, 'core/tarla_rehberi.html', context)


def tarla_rehberi_detay_view(request, problem_slug):
    from .models import FieldGuideItem
    from django.shortcuts import redirect
    try:
        data = FieldGuideItem.objects.get(slug=problem_slug)
    except FieldGuideItem.DoesNotExist:
        return redirect('tarla_rehberi')
        
    return render(request, 'core/tarla_rehberi_detay.html', {'data': data})


@staff_member_required
def add_guide_item_view(request):
    from .forms import FieldGuideItemForm
    from .models import FieldGuideItem
    
    if request.method == 'POST':
        form = FieldGuideItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            
            # Parse list fields from request POST
            symptoms = request.POST.getlist('symptoms')
            item.symptoms = [s.strip() for s in symptoms if s.strip()]
            
            preventative = request.POST.getlist('preventative_measures')
            item.preventative_measures = [pm.strip() for pm in preventative if pm.strip()]
            
            pro_titles = request.POST.getlist('pro_title')
            pro_descs = request.POST.getlist('pro_desc')
            pros = []
            for title, desc in zip(pro_titles, pro_descs):
                if title.strip() or desc.strip():
                    pros.append({"title": title.strip(), "desc": desc.strip()})
            item.pros = pros
            
            con_titles = request.POST.getlist('con_title')
            con_descs = request.POST.getlist('con_desc')
            cons = []
            for title, desc in zip(con_titles, con_descs):
                if title.strip() or desc.strip():
                    cons.append({"title": title.strip(), "desc": desc.strip()})
            item.cons = cons
            
            item.save()
            return redirect('tarla_rehberi')
    else:
        form = FieldGuideItemForm()
        
    return render(request, 'core/tarla_rehberi_form.html', {
        'form': form,
        'edit_mode': False,
        'symptoms_list': [],
        'preventative_list': [],
        'pros_list': [],
        'cons_list': []
    })


@staff_member_required
def update_guide_item_view(request, problem_slug):
    from .models import FieldGuideItem
    from .forms import FieldGuideItemForm
    
    item = get_object_or_404(FieldGuideItem, slug=problem_slug)
    if request.method == 'POST':
        form = FieldGuideItemForm(request.POST, instance=item)
        if form.is_valid():
            updated_item = form.save(commit=False)
            
            # Parse list fields from request POST
            symptoms = request.POST.getlist('symptoms')
            updated_item.symptoms = [s.strip() for s in symptoms if s.strip()]
            
            preventative = request.POST.getlist('preventative_measures')
            updated_item.preventative_measures = [pm.strip() for pm in preventative if pm.strip()]
            
            pro_titles = request.POST.getlist('pro_title')
            pro_descs = request.POST.getlist('pro_desc')
            pros = []
            for title, desc in zip(pro_titles, pro_descs):
                if title.strip() or desc.strip():
                    pros.append({"title": title.strip(), "desc": desc.strip()})
            updated_item.pros = pros
            
            con_titles = request.POST.getlist('con_title')
            con_descs = request.POST.getlist('con_desc')
            cons = []
            for title, desc in zip(con_titles, con_descs):
                if title.strip() or desc.strip():
                    cons.append({"title": title.strip(), "desc": desc.strip()})
            updated_item.cons = cons
            
            updated_item.save()
            return redirect('tarla_rehberi_detay', problem_slug=updated_item.slug)
    else:
        form = FieldGuideItemForm(instance=item)
        
    return render(request, 'core/tarla_rehberi_form.html', {
        'form': form,
        'edit_mode': True,
        'item': item,
        'symptoms_list': item.symptoms,
        'preventative_list': item.preventative_measures,
        'pros_list': item.pros,
        'cons_list': item.cons
    })


@staff_member_required
def delete_guide_item_view(request, problem_slug):
    from .models import FieldGuideItem
    item = get_object_or_404(FieldGuideItem, slug=problem_slug)
    if request.method == 'POST':
        item.delete()
        return redirect('tarla_rehberi')
    return redirect('tarla_rehberi_detay', problem_slug=problem_slug)


