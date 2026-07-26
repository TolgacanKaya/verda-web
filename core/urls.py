from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('hakkimizda/', views.about_view, name='about'),
    path('kullanim-kosullari/', views.terms_view, name='terms'),
    path('gizlilik-politikasi/', views.privacy_view, name='privacy'),
    path('iletisim/', views.contact_view, name='contact'),
]