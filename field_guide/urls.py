from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.tarla_rehberi_view, name='tarla_rehberi'),
    path('ekle/', views.add_guide_item_view, name='add_guide_item'),
    path('api/all/', api_views.get_field_guide_api, name='get_field_guide_api'),
    path('<slug:problem_slug>/', views.tarla_rehberi_detay_view, name='tarla_rehberi_detay'),
    path('<slug:problem_slug>/guncelle/', views.update_guide_item_view, name='update_guide_item'),
    path('<slug:problem_slug>/sil/', views.delete_guide_item_view, name='delete_guide_item'),
]
