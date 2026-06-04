from django.contrib import admin
from .models import FarmerProfile

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location']
    search_fields = ['user__username', 'location']
    # ManyToMany (Çoklu) bitki seçimi alanını admin panelinde yan yana şık göstermek için:
    filter_horizontal = ['grown_plants']