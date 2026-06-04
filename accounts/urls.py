from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('kayit/', views.register_view, name='register'),
    path('giris/', views.login_view, name='login'),
    path('cikis/', views.logout_view, name='logout'),
    path('profil/', views.profile_detail_view, name='profile_detail'),  # YENİ VİTRİN
    path('ayarlar/', views.profile_settings_view, name='profile_settings'),  # YENİ AYARLAR YOLU
    path('api/hava-durumu/', views.weather_api_view, name='weather_api'),
    path('api/profil/', api_views.get_profile_api, name='get_profile_api'),
    path('api/giris/', api_views.api_login, name='api_login'),
    path('api/kayit/', api_views.api_register, name='api_register'),
    path('api/favori/', api_views.toggle_favorite_api, name='toggle_favorite_api'),
    path('api/favori-ai/', api_views.favorite_plants_ai_api, name='favorite_plants_ai_api'),
]