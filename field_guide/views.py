from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import FieldGuideItem
from .forms import FieldGuideItemForm
from django.core.paginator import Paginator
from django.db.models import Q

def tarla_rehberi_view(request):
    # 1. Filtre parametrelerini al
    season_slug = request.GET.get('season', 'ilkbahar').lower()
    q = request.GET.get('q', '').strip()
    tag = request.GET.get('tag', 'all').strip()
    page = request.GET.get('page', 1)

    # Mevsim haritası (Slug -> DB Değeri)
    season_map = {
        'ilkbahar': 'İlkbahar',
        'yaz': 'Yaz',
        'sonbahar': 'Sonbahar',
        'kis': 'Kış'
    }
    db_season = season_map.get(season_slug, 'İlkbahar')

    # 2. Queryset Filtrele
    items = FieldGuideItem.objects.filter(season=db_season)

    if q:
        items = items.filter(
            Q(title__icontains=q) | 
            Q(scientific_name__icontains=q) | 
            Q(description__icontains=q)
        )

    if tag and tag != 'all':
        if tag == 'Hastalık':
            items = items.filter(
                Q(category__icontains='Hastalık') |
                Q(category__icontains='Bakteri') |
                Q(category__icontains='Fungus') |
                Q(category__icontains='Mantar') |
                Q(category__icontains='Virüs')
            )
        elif tag == 'Zararlı':
            items = items.filter(category__icontains='Zararlı')
        else:
            items = items.filter(risk_level=tag)

    # 3. Sayfalama (Bento Grid için sayfa başına 6 kayıt idealdir)
    paginator = Paginator(items, 6)
    page_obj = paginator.get_page(page)

    # 4. Üretim Modelleri (Karşılaştırma kartları her zaman tam yüklenir)
    uretim_modelleri = FieldGuideItem.objects.filter(season='Genel')

    context = {
        'page_obj': page_obj,
        'uretim_modelleri': uretim_modelleri,
        'current_season': season_slug,
        'current_q': q,
        'current_tag': tag,
    }

    # AJAX isteği ise sadece grid ve pagination barını içeren partial'ı dönüyoruz
    if request.GET.get('ajax') == '1' or request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'core/partials/tarla_rehberi_grid.html', context)

    return render(request, 'core/tarla_rehberi.html', context)



def tarla_rehberi_detay_view(request, problem_slug):
    try:
        data = FieldGuideItem.objects.get(slug=problem_slug)
    except FieldGuideItem.DoesNotExist:
        return redirect('tarla_rehberi')
        
    return render(request, 'core/tarla_rehberi_detay.html', {'data': data})


@staff_member_required
def add_guide_item_view(request):
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
    item = get_object_or_404(FieldGuideItem, slug=problem_slug)
    if request.method == 'POST':
        item.delete()
        return redirect('tarla_rehberi')
    return redirect('tarla_rehberi_detay', problem_slug=problem_slug)
