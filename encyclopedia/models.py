from django.db import models

class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('Sebzeler', 'Sebzeler'),
        ('Meyveler', 'Meyveler'),
        ('Tahıllar', 'Tahıllar'),
        ('Baharat & Otlar', 'Baharat & Otlar'),
        ('Diğer', 'Diğer'),
    ]
    name = models.CharField(max_length=100, unique=True, verbose_name="Bitki Adı (Örn: Domates)")
    scientific_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Bilimsel Adı")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Diğer', verbose_name="Kategori")
    description = models.TextField(blank=True, null=True, verbose_name="Genel Bilgi")
    image = models.ImageField(upload_to='plants/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bitki"
        verbose_name_plural = "Bitkiler"


class Disease(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='diseases', verbose_name="Ait Olduğu Bitki")
    name = models.CharField(max_length=150, verbose_name="Hastalık Adı (Örn: Erken Yanıklık)")
    symptoms = models.TextField(verbose_name="Belirtiler")
    organic_treatment = models.TextField(blank=True, null=True, verbose_name="Organik Çözüm")
    chemical_treatment = models.TextField(blank=True, null=True, verbose_name="Kimyasal Çözüm")
    prevention = models.TextField(blank=True, null=True, verbose_name="Önlem ve Tavsiyeler")
    ai_class_id = models.IntegerField(blank=True, null=True, verbose_name="Yapay Zeka Sınıf ID (Opsiyonel)")

    def __str__(self):
        return f"{self.plant.name} - {self.name}"

    class Meta:
        verbose_name = "Hastalık"
        verbose_name_plural = "Hastalıklar"