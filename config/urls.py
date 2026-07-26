from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tarla-rehberi/', include('field_guide.urls')),
    path('', include('core.urls')), # Kurumsal sayfa yönlendirmeleri
    path('admin/', admin.site.urls),
    path('teshis/', include('diagnostics.urls')), # YENİ EKLENEN SATIR
    path('ansiklopedi/', include('encyclopedia.urls')),
    path('hesap/', include('accounts.urls')),
    path('meydan/', include('community.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Reload trigger final done
