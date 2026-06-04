from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('hakkimizda/', views.about_view, name='about'),
    path('kullanim-kosullari/', views.terms_view, name='terms'),
    path('gizlilik-politikasi/', views.privacy_view, name='privacy'),
    path('iletisim/', views.contact_view, name='contact'),
    path('tarla-rehberi/', views.tarla_rehberi_view, name='tarla_rehberi'),
    path('tarla-rehberi/ekle/', views.add_guide_item_view, name='add_guide_item'),
    path('tarla-rehberi/<slug:problem_slug>/', views.tarla_rehberi_detay_view, name='tarla_rehberi_detay'),
    path('tarla-rehberi/<slug:problem_slug>/guncelle/', views.update_guide_item_view, name='update_guide_item'),
    path('tarla-rehberi/<slug:problem_slug>/sil/', views.delete_guide_item_view, name='delete_guide_item'),
]