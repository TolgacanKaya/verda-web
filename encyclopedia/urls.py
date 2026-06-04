from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.encyclopedia_view, name='encyclopedia'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plant/<int:pk>/guncelle/', views.update_plant, name='update_plant'), # GÜNCELLEME
    path('plant/<int:plant_pk>/hastalik-ekle/', views.add_disease, name='add_disease'), # TEŞHİS EKLEME
    path('ekle/', views.add_plant, name='add_plant'),
    # YENİ EKLENEN HASTALIK GÜNCELLEME VE SİLME
    path('hastalik/<int:pk>/guncelle/', views.update_disease, name='update_disease'),
    path('hastalik/<int:pk>/sil/', views.delete_disease, name='delete_disease'),
    path('api/ai-asistan/', views.plant_chat_api, name='plant_chat_api'),
    path('api/all/', api_views.get_encyclopedia_api, name='get_encyclopedia_api'),
]