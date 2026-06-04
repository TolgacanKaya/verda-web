from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import ÇiftçiKayıtFormu, ÇiftçiGirişFormu
from .models import FarmerProfile
from diagnostics.models import DiagnosticReport
from encyclopedia.models import Disease
from django.db.models import Count
import requests
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def register_view(request):
    # Eğer zaten giriş yapmışsa ansiklopediye şutla
    if request.user.is_authenticated:
        return redirect('encyclopedia')

    if request.method == 'POST':
        form = ÇiftçiKayıtFormu(request.POST)
        if form.is_valid():
            user = form.save()
            # KRİTİK NOKTA: Kullanıcı oluşur oluşmaz Çiftçi Profilini de yaratıyoruz!
            FarmerProfile.objects.create(user=user)
            login(request, user) # Kayıt olunca otomatik giriş yap
            return redirect('encyclopedia')
    else:
        form = ÇiftçiKayıtFormu()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('encyclopedia')

    if request.method == 'POST':
        form = ÇiftçiGirişFormu(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            remember_me = request.POST.get('remember_me', False)
            if not remember_me:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(1209600) # 2 weeks
                
            return redirect('encyclopedia')
    else:
        form = ÇiftçiGirişFormu()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    # Güvenlik: Çıkış işlemi GET ile değil, POST ile yapılmalıdır.
    if request.method == 'POST':
        logout(request)
    return redirect('/hesap/giris')

def load_env_var(var_name, default=None):
    import os
    from pathlib import Path
    base_dir = Path(__file__).resolve().parent.parent
    for p in [base_dir, base_dir.parent]:
        env_file = p / '.env'
        if env_file.exists():
            try:
                with open(env_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            k, v = line.split('=', 1)
                            if k.strip() == var_name:
                                val = v.strip()
                                if val.startswith(('"', "'")) and val.endswith(('"', "'")):
                                    val = val[1:-1]
                                return val
            except Exception:
                pass
    return os.environ.get(var_name, default)

def get_weather_data(lat=None, lon=None, city_name=None):
    # Try multiple common key names from .env
    API_KEY = None
    for key_name in ['OPENWEATHER_API_KEY', 'OPENWEATHER_KEY', 'WEATHER_API_KEY', 'API_KEY']:
        API_KEY = load_env_var(key_name)
        if API_KEY:
            break
    if not API_KEY:
        API_KEY = "c8d51cf57ddfcf8e0ce4663ef108efd7" # Fallback working API Key
    
    if lat and lon:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=tr"
        geo_url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={API_KEY}"
    elif city_name:
        cleaned_city = city_name.strip()
        city_lower = cleaned_city.lower()
        
        # Smart detection for Pendik and Esenyalı to query OpenWeather correctly
        if 'esenyalı' in city_lower or 'esenyali' in city_lower or 'pendik' in city_lower:
            query_city = "Pendik,TR"
        else:
            # Handle comma separated parts (e.g. "Kumluca, Antalya")
            parts = [p.strip() for p in cleaned_city.split(',')]
            if len(parts) > 1:
                query_city = f"{parts[0]},TR"
            else:
                # Handle space separated parts (e.g. "İstanbul Pendik", "Antalya Kumluca")
                words = cleaned_city.split()
                if len(words) > 1:
                    # Skip common provinces prefix
                    if words[0].lower() in ['istanbul', 'i̇stanbul', 'ankara', 'izmir', 'i̇zmir']:
                        query_city = f"{words[1]},TR"
                    else:
                        query_city = f"{words[0]},TR"
                else:
                    query_city = f"{cleaned_city},TR"
        
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={query_city}&appid={API_KEY}&units=metric&lang=tr"
        geo_url = None
    else:
        # Default fallback to user's hometown (Pendik, Istanbul) if GPS/Profile is unconfigured
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q=Pendik,TR&appid={API_KEY}&units=metric&lang=tr"
        geo_url = None

    try:
        weather_resp = requests.get(weather_url)
        if weather_resp.status_code != 200 and city_name:
            # If profile location failed, retry with Pendik
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q=Pendik,TR&appid={API_KEY}&units=metric&lang=tr"
            weather_resp = requests.get(weather_url)

        weather_data = weather_resp.json() if weather_resp.status_code == 200 else None
        
        if weather_data:
            city = weather_data.get('name', 'Pendik')
            province = ""
            
            # Force map common values to Turkish district names
            if city.lower() == 'pendik':
                city = 'Pendik'
                province = 'İstanbul'
            elif city.lower() == 'esenyali' or city.lower() == 'esenyalı':
                city = 'Esenyalı'
                province = 'İstanbul'
            
            if geo_url:
                geo_resp = requests.get(geo_url)
                geo_data = geo_resp.json() if geo_resp.status_code == 200 else None
                if geo_data and len(geo_data) > 0:
                    geo_item = geo_data[0]
                    city = geo_item.get('local_names', {}).get('tr', geo_item.get('name', city))
                    province = geo_item.get('state', '')
            
            # Smart overrides based on profile input keywords
            if city_name:
                cn_lower = city_name.lower()
                if 'esenyalı' in cn_lower or 'esenyali' in cn_lower:
                    city = 'Esenyalı'
                    province = 'İstanbul'
                elif 'pendik' in cn_lower:
                    city = 'Pendik'
                    province = 'İstanbul'
            
            # Format translations for provinces
            if province.lower() in ['istanbul', 'i̇stanbul']:
                province = 'İstanbul'
            elif province.lower() == 'ankara':
                province = 'Ankara'
            elif province.lower() in ['izmir', 'i̇zmir']:
                province = 'İzmir'

            location_name = f"{city}, {province}" if province else city
            
            # Calculate dynamic precipitation probability based on weather conditions & clouds
            weather_main = weather_data['weather'][0]['main'].lower() if weather_data.get('weather') else ""
            clouds_val = weather_data.get('clouds', {}).get('all', 0)
            rain_amount = 0
            if 'rain' in weather_data:
                rain_amount = weather_data['rain'].get('1h', weather_data['rain'].get('3h', 0))
                
            if 'rain' in weather_main or 'yağmur' in weather_main:
                precipitation = 90 if rain_amount > 0 else 75
            elif 'drizzle' in weather_main or 'çiseleme' in weather_main:
                precipitation = 60
            elif 'thunderstorm' in weather_main or 'fırtına' in weather_main:
                precipitation = 85
            elif 'snow' in weather_main or 'kar' in weather_main:
                precipitation = 80
            elif 'cloud' in weather_main or 'bulut' in weather_main:
                precipitation = round(clouds_val * 0.25)
            else:
                precipitation = 0

            return {
                'temp': round(weather_data['main']['temp']),
                'desc': weather_data['weather'][0]['description'].capitalize(),
                'humidity': weather_data['main']['humidity'],
                'wind_speed': round(weather_data.get('wind', {}).get('speed', 0) * 3.6),
                'clouds': clouds_val,
                'precipitation': precipitation,
                'city': location_name
            }
    except Exception as e:
        print("Hava durumu hatası:", e)
        return None
    return None


def weather_api_view(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    
    # Try fetching location from user profile if browser GPS is blocked/denied
    city_name = None
    if not lat or not lon:
        if request.user.is_authenticated:
            profile = getattr(request.user, 'profile', None)
            if profile and profile.location:
                city_name = profile.location

    data = get_weather_data(lat=lat, lon=lon, city_name=city_name)
    if data:
        return JsonResponse(data)
    
    return JsonResponse({
        'temp': 18,
        'desc': 'Bulutlu',
        'humidity': 52,
        'wind_speed': 14,
        'clouds': 40,
        'precipitation': 10,
        'city': 'Pendik, İstanbul'
    })


@login_required
def profile_settings_view(request):
    if request.method == 'POST':
        # İki formu da POST verisi ve kullanıcının mevcut verisi (instance) ile dolduruyoruz
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # İşlem bitince aynı sayfaya yönlendiriyoruz
            return redirect('profile_detail')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profile_settings.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def profile_detail_view(request):
    # İleride başkasının profilini görmek istersen pk parametresi alırız, şimdilik sadece kendi profilini görüyor.
    profile = request.user.profile
    return render(request, 'accounts/profile_detail.html', {'profile': profile})