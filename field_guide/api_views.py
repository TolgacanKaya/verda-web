from django.http import JsonResponse
from .models import FieldGuideItem

def get_field_guide_api(request):
    """
    Returns all field guide items as JSON for the mobile application.
    """
    items = FieldGuideItem.objects.all()
    
    # Filtreleme (Sezon, Arama & Risk Etiketi)
    season = request.GET.get('season')
    search_query = request.GET.get('search')
    risk_tag = request.GET.get('risk_tag')
    
    if season:
        items = items.filter(season=season)
        
    if search_query:
        from django.db.models import Q
        items = items.filter(
            Q(title__icontains=search_query) | 
            Q(scientific_name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
        
    if risk_tag and risk_tag != 'Tümü':
        if risk_tag == 'Kritik':
            items = items.filter(risk_level__iexact='çok yüksek')
        elif risk_tag == 'Yüksek Risk':
            items = items.filter(risk_level__iexact='yüksek')
        elif risk_tag == 'Hastalıklar':
            from django.db.models import Q
            items = items.filter(Q(category__icontains='hastalık') | Q(category__icontains='fungus'))
        elif risk_tag == 'Zararlılar':
            from django.db.models import Q
            items = items.filter(Q(category__icontains='zararlı') | Q(category__icontains='istila'))

    # Sayfalama (Pagination) Desteği
    page_num = request.GET.get('page')
    per_page = request.GET.get('per_page', 10)
    
    if page_num:
        from django.core.paginator import Paginator, EmptyPage
        try:
            per_page = int(per_page)
        except ValueError:
            per_page = 10
            
        paginator = Paginator(items, per_page)
        try:
            page_obj = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({'status': 'success', 'data': [], 'has_next': False, 'total_pages': paginator.num_pages})
        except Exception:
            page_obj = paginator.page(1)
            
        items_to_serialize = page_obj.object_list
        has_next = page_obj.has_next()
        total_pages = paginator.num_pages
    else:
        items_to_serialize = items
        has_next = False
        total_pages = 1

    data = []
    for item in items_to_serialize:
        data.append({
            'id': item.id,
            'slug': item.slug,
            'title': item.title,
            'scientific_name': item.scientific_name or "",
            'category': item.category,
            'season': item.season,
            'risk_level': item.risk_level,
            'description': item.description,
            'symptoms': item.symptoms,
            'favorable_conditions': item.favorable_conditions,
            'case_scenario': item.case_scenario,
            'organic_recipe_name': item.organic_recipe_name,
            'organic_recipe_prep': item.organic_recipe_prep,
            'organic_recipe_app': item.organic_recipe_app,
            'preventative_measures': item.preventative_measures,
            'recipe_preview': item.recipe_preview or "",
            'pros': item.pros,
            'cons': item.cons,
        })
    return JsonResponse({'status': 'success', 'data': data, 'has_next': has_next, 'total_pages': total_pages})
