from django.contrib import admin
from .models import FieldGuideItem

@admin.register(FieldGuideItem)
class FieldGuideItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'season', 'risk_level')
    list_filter = ('season', 'category', 'risk_level')
    search_fields = ('title', 'scientific_name', 'description')
    prepopulated_fields = {'slug': ('title',)}

