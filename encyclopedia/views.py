from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Plant, Disease
from .forms import PlantForm, DiseaseForm
from django.db.models import Q
import json
from django.http import JsonResponse
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt

def encyclopedia_view(request):
    query = request.GET.get('q')  # Arama çubuğundan gelen veri
    if query:
        plants = Plant.objects.filter(
            Q(name__icontains=query) | Q(scientific_name__icontains=query)
        ).prefetch_related('diseases')
    else:
        plants = Plant.objects.prefetch_related('diseases').all()

    return render(request, 'encyclopedia/encyclopedia.html', {'plants': plants, 'query': query})


def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    is_favorite = False
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        if profile:
            is_favorite = profile.favorite_plants.filter(pk=plant.pk).exists()
    return render(request, 'encyclopedia/plant_detail.html', {'plant': plant, 'is_favorite': is_favorite})


@staff_member_required
def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('encyclopedia')
    else:
        form = PlantForm()

    return render(request, 'encyclopedia/add_plant.html', {'form': form})

@staff_member_required
def update_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', pk=plant.pk)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'encyclopedia/add_plant.html', {'form': form, 'edit_mode': True})

@staff_member_required
def add_disease(request, plant_pk):
    plant = get_object_or_404(Plant, pk=plant_pk)
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            disease = form.save(commit=False)
            disease.plant = plant # Hastalığı ilgili bitkiye bağlıyoruz
            disease.save()
            return redirect('plant_detail', pk=plant.pk)
    else:
        form = DiseaseForm()
    return render(request, 'encyclopedia/add_disease.html', {'form': form, 'plant': plant})


@staff_member_required
def update_disease(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    plant = disease.plant  # Formda geri dönebilmek için bitkiyi alıyoruz

    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', pk=plant.pk)
    else:
        form = DiseaseForm(instance=disease)

    # Mevcut add_disease.html'i tekrar kullanıyoruz, edit_mode göndererek
    return render(request, 'encyclopedia/add_disease.html', {'form': form, 'plant': plant, 'edit_mode': True})


@staff_member_required
def delete_disease(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    plant_pk = disease.plant.pk  # Silindikten sonra bitki sayfasına dönmek için

    if request.method == 'POST':
        disease.delete()

    return redirect('plant_detail', pk=plant_pk)


@csrf_exempt
def plant_chat_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            plant_name = data.get('plant_name', 'Bitki')
            question = data.get('question', '')

            # Görseldeki o ...k1Ws ile biten anahtarını buraya yapıştır
            genai.configure(api_key="AIzaSyBOWZwCsSc4yGJjuf3zLSbEugxdUA9k1Ws")
            # Güncel kütüphane ile bu model artık sorunsuz çalışacak
            model = genai.GenerativeModel('gemini-2.5-flash')

            prompt = f"Sen tecrübeli bir ziraat mühendisisin. Çiftçi sana '{plant_name}' bitkisi hakkında şu soruyu soruyor: '{question}'. Çok kısa, samimi ve madde madde yanıt ver."

            response = model.generate_content(prompt)
            return JsonResponse({'answer': response.text})

        except Exception as e:
            print(f"🚨 GEMİNİ HATASI: {e}")
            return JsonResponse({'answer': f"Bağlantı hatası: {str(e)}"})

    return JsonResponse({'error': 'Geçersiz istek'}, status=400)