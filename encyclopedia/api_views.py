from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Plant

@csrf_exempt
def get_encyclopedia_api(request):
    """Mobil uygulama için tüm bitki ve hastalık verilerini döner."""
    if request.method == 'GET':
        username = request.GET.get('username')
        fav_plant_ids = set()
        if username:
            from accounts.models import FarmerProfile
            profile = FarmerProfile.objects.filter(user__username=username).first()
            if profile:
                fav_plant_ids = set(profile.favorite_plants.values_list('id', flat=True))

        plants = Plant.objects.prefetch_related('diseases').all()
        
        # Filtreleme (Kategori & Arama)
        category = request.GET.get('category')
        search_query = request.GET.get('search')
        
        if category and category != 'Tümü':
            plants = plants.filter(category=category)
            
        if search_query:
            from django.db.models import Q
            plants = plants.filter(Q(name__icontains=search_query) | Q(scientific_name__icontains=search_query))
        
        # Sayfalama (Pagination) Desteği
        page_num = request.GET.get('page')
        per_page = request.GET.get('per_page', 10)
        
        if page_num:
            from django.core.paginator import Paginator, EmptyPage
            try:
                per_page = int(per_page)
            except ValueError:
                per_page = 10
                
            paginator = Paginator(plants, per_page)
            try:
                page_obj = paginator.page(page_num)
            except EmptyPage:
                return JsonResponse({'status': 'success', 'data': [], 'has_next': False, 'total_pages': paginator.num_pages})
            except Exception:
                page_obj = paginator.page(1)
                
            plants_to_serialize = page_obj.object_list
            has_next = page_obj.has_next()
            total_pages = paginator.num_pages
        else:
            plants_to_serialize = plants
            has_next = False
            total_pages = 1

        data = []
        for plant in plants_to_serialize:
            plant_data = {
                'id': plant.id,
                'name': plant.name,
                'scientific_name': plant.scientific_name,
                'category': plant.category,
                'description': plant.description,
                'image': request.build_absolute_uri(plant.image.url) if plant.image else "",
                'is_favorite': plant.id in fav_plant_ids,
                'diseases': []
            }
            for disease in plant.diseases.all():
                plant_data['diseases'].append({
                    'id': disease.id,
                    'name': disease.name,
                    'symptoms': disease.symptoms,
                    'organic_treatment': disease.organic_treatment,
                    'chemical_treatment': disease.chemical_treatment,
                    'prevention': disease.prevention,
                })
            data.append(plant_data)
            
        return JsonResponse({'status': 'success', 'data': data, 'has_next': has_next, 'total_pages': total_pages})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
