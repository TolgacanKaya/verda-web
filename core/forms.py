from django import forms
from .models import FieldGuideItem

class FieldGuideItemForm(forms.ModelForm):
    class Meta:
        model = FieldGuideItem
        fields = [
            'slug', 'title', 'scientific_name', 'category', 'season', 'risk_level',
            'description', 'organic_recipe_name', 'organic_recipe_prep', 
            'organic_recipe_app', 'recipe_preview', 'favorable_conditions', 'case_scenario'
        ]
        widgets = {
            'slug': forms.TextInput(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'placeholder': 'Örn: demir-klorozu'
            }),
            'title': forms.TextInput(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'placeholder': 'Örn: Demir Klorozu ve Yaprak Sararması'
            }),
            'scientific_name': forms.TextInput(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'placeholder': 'Örn: Fizyolojik Demir (Fe) Noksanlığı'
            }),
            'category': forms.TextInput(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'placeholder': 'Örn: Toprak Fizyolojisi'
            }),
            'season': forms.Select(choices=[
                ('İlkbahar', 'İlkbahar'),
                ('Yaz', 'Yaz'),
                ('Sonbahar', 'Sonbahar'),
                ('Kış', 'Kış'),
                ('Genel', 'Genel (Üretim Modeli)'),
            ], attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all'
            }),
            'risk_level': forms.TextInput(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'placeholder': 'Örn: Yüksek, Orta-Yüksek, Düşük-Orta'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'rows': 3,
                'placeholder': 'Bitki veya sisteme ait kısa genel açıklama...'
            }),
            'favorable_conditions': forms.Textarea(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'rows': 2,
                'placeholder': 'Tetikleyici iklimsel risk koşulları veya yetiştirme ortam parametreleri...'
            }),
            'case_scenario': forms.Textarea(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'rows': 4,
                'placeholder': 'Örnek bir saha vaka raporu yazın (Doğa bilimci günlüğü tarzı)...'
            }),
            'organic_recipe_name': forms.TextInput(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'placeholder': 'Örn: Kükürtlü Organik Demir Şelatı'
            }),
            'organic_recipe_prep': forms.Textarea(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'rows': 3,
                'placeholder': 'Reçete hazırlık aşamaları...'
            }),
            'organic_recipe_app': forms.Textarea(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'rows': 3,
                'placeholder': 'Sahada veya sera içerisinde uygulama adımları...'
            }),
            'recipe_preview': forms.Textarea(attrs={
                'class': 'block w-full rounded-2xl border border-white bg-white/50 backdrop-blur-md px-4 py-3 text-sm font-semibold text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 shadow-inner transition-all',
                'rows': 2,
                'placeholder': 'Ana sayfadaki mevsimlik kartlarda görünecek kısa tek cümlelik önizleme...'
            }),
        }
