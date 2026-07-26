from django.contrib import admin
from .models import FieldGuideItem

@admin.register(FieldGuideItem)
class FieldGuideItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'season', 'risk_level', 'category')
    search_fields = ('title', 'scientific_name', 'category')
    prepopulated_fields = {'slug': ('title',)}
