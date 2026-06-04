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
        data = []
        for plant in plants:
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
            
        return JsonResponse({'status': 'success', 'data': data})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
