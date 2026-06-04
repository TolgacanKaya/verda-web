from django import forms
from .models import Plant, Disease

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'scientific_name', 'category', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50', 'placeholder': 'Örn: Domates'}),
            'scientific_name': forms.TextInput(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50', 'placeholder': 'Örn: Solanum lycopersicum'}),
            'category': forms.Select(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50'}),
            'description': forms.Textarea(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50', 'rows': 4}),
            # Dosya yükleme butonu için özel Tailwind sınıfları
            'image': forms.FileInput(attrs={'class': 'block w-full text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-brand-50 file:text-brand-700 hover:file:bg-brand-100 transition-colors cursor-pointer'}),
        }

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name', 'symptoms', 'organic_treatment', 'chemical_treatment', 'prevention', 'ai_class_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 px-4 py-3 bg-gray-50', 'placeholder': 'Hastalık Adı'}),
            'symptoms': forms.Textarea(attrs={'class': 'block w-full rounded-xl border-gray-300 px-4 py-3 bg-gray-50', 'rows': 3}),
            'organic_treatment': forms.Textarea(attrs={'class': 'block w-full rounded-xl border-gray-300 px-4 py-3 bg-gray-50', 'rows': 3}),
            'chemical_treatment': forms.Textarea(attrs={'class': 'block w-full rounded-xl border-gray-300 px-4 py-3 bg-gray-50', 'rows': 3}),
            'prevention': forms.Textarea(attrs={'class': 'block w-full rounded-xl border-gray-300 px-4 py-3 bg-gray-50', 'rows': 3}),
            'ai_class_id': forms.NumberInput(attrs={'class': 'block w-full rounded-xl border-gray-300 px-4 py-3 bg-gray-50', 'placeholder': 'Model Sınıf ID (0-14)'}),
        }