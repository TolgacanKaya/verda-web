from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.diagnose_view, name='diagnose'),
    path('api/diagnose/', api_views.diagnose_api, name='api_diagnose'),
    path('gecmis/', views.diagnostic_history_view, name='diagnostic_history'),
    path('rapor/<int:pk>/', views.diagnostic_detail_view, name='diagnostic_detail'),
    path('rapor/<int:pk>/sil/', views.delete_diagnostic_view, name='delete_diagnostic'),
    path('api/rapor/<int:pk>/sil/', api_views.delete_diagnostic_api, name='api_delete_diagnostic'),
]