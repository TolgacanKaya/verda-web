from django.contrib import admin
from .models import Plant, Disease

# Admin panelinde tabloların daha şık görünmesi için ayarlar
class DiseaseInline(admin.TabularInline):
    model = Disease
    extra = 1 # Yeni hastalık eklemek için hazır 1 boş satır

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')
    search_fields = ('name',)
    inlines = [DiseaseInline] # Bitkinin içindeyken hastalıklarını da görebilmek için

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'plant', 'ai_class_id')
    list_filter = ('plant',)
    search_fields = ('name',)