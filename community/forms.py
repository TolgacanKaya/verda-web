from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'related_plant']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50', 'rows': 3, 'placeholder': 'Tarlanızda ne var? Sorunuzu veya tecrübenizi paylaşın...'}),
            'image': forms.FileInput(attrs={'class': 'block w-full text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-brand-50 file:text-brand-700 hover:file:bg-brand-100 transition-colors cursor-pointer'}),
            'related_plant': forms.Select(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50'})
        }
        labels = {
            'content': 'Ne Sormak İstiyorsunuz?',
            'image': 'Fotoğraf (Zorunlu)',
            'related_plant': 'İlgili Bitki (Opsiyonel)'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50', 'rows': 2, 'placeholder': 'Çözümünüzü veya fikrinizi yazın...'}),
        }
        labels = {'content': ''}