from django.db import models
from django.contrib.auth.models import User
from encyclopedia.models import Plant

class FarmerProfile(models.Model):
    EXPERIENCE_LEVELS = (
        ('newbie', 'Yeni Başlayan'),
        ('experienced', 'Deneyimli Çiftçi'),
        ('expert', 'Ziraat Uzmanı'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True, verbose_name="Profil Fotoğrafı")
    cover_picture = models.ImageField(upload_to='covers/', null=True, blank=True, verbose_name="Kapak Fotoğrafı")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Konum (İl/İlçe)")
    bio = models.TextField(blank=True, null=True, verbose_name="Hakkımda (Kısa Biyografi)")

    # Çiftçinin tarlasındaki bitkiler (Çoklu seçim - ManyToMany)
    grown_plants = models.ManyToManyField(Plant, blank=True, verbose_name="Yetiştirdiğim Bitkiler")
    
    # Çiftçinin favori bitkileri (Çoklu seçim - ManyToMany)
    favorite_plants = models.ManyToManyField(Plant, blank=True, related_name='favorited_by', verbose_name="Favori Bitkilerim")

    def __str__(self):
        return f"{self.user.username} Profili"

    class Meta:
        verbose_name = "Çiftçi Profili"
        verbose_name_plural = "Çiftçi Profilleri"