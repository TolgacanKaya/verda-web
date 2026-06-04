from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from encyclopedia.models import Plant
from .models import FarmerProfile

# Ortak Tailwind sınıflarımız
input_classes = 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50 mb-4'


class ÇiftçiKayıtFormu(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")  # İstersen buraya first_name falan da ekleyebilirsin

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Kullanıcı Adı"
        self.fields['email'].label = "E-posta Adresi"
        for field in self.fields.values():
            field.widget.attrs['class'] = input_classes


class ÇiftçiGirişFormu(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Kullanıcı Adı"
        self.fields['password'].label = "Şifre"
        for field in self.fields.values():
            field.widget.attrs['class'] = input_classes


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "Adınız"
        self.fields['last_name'].label = "Soyadınız"
        self.fields['email'].label = "E-Posta Adresi"
        for field in self.fields.values():
            field.widget.attrs[
                'class'] = 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 focus:border-brand-500 px-4 py-3 bg-gray-50 mb-4'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ['profile_picture', 'cover_picture', 'location', 'bio', 'grown_plants']
        widgets = {
            'location': forms.TextInput(attrs={
                'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 px-4 py-3 bg-gray-50',
                'placeholder': 'Örn: Antalya, Kumluca'}),
            'bio': forms.Textarea(attrs={
                'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 px-4 py-3 bg-gray-50',
                'rows': 3, 'placeholder': 'Tarlanız ve tecrübeleriniz hakkında kısaca...'}),
            'grown_plants': forms.SelectMultiple(attrs={
                'class': 'block w-full rounded-xl border-gray-300 shadow-sm focus:ring-brand-500 px-4 py-3 bg-gray-50'}),
            'profile_picture': forms.FileInput(attrs={
                'class': 'block w-full text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-brand-50 file:text-brand-700 hover:file:bg-brand-100 transition-colors cursor-pointer'}),
            'cover_picture': forms.FileInput(attrs={
                'class': 'block w-full text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-brand-50 file:text-brand-700 hover:file:bg-brand-100 transition-colors cursor-pointer'}),
        }
        labels = {
            'profile_picture': 'Profil Fotoğrafı',
            'cover_picture': 'Kapak Fotoğrafı',
            'location': 'Konum',
            'bio': 'Hakkımda',
            'grown_plants': 'Tarlamdaki Bitkiler'
        }