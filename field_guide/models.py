from django.db import models

class FieldGuideItem(models.Model):
    slug = models.SlugField(unique=True, verbose_name="URL Slug")
    title = models.CharField(max_length=200, verbose_name="Başlık")
    scientific_name = models.CharField(max_length=250, blank=True, null=True, verbose_name="Bilimsel Adı")
    category = models.CharField(max_length=100, verbose_name="Kategori")
    season = models.CharField(max_length=50, verbose_name="Dönem/Mevsim") # İlkbahar, Yaz, Sonbahar, Kış, Genel
    risk_level = models.CharField(max_length=50, verbose_name="Risk Seviyesi")
    description = models.TextField(verbose_name="Açıklama")
    
    # Detay Raporu Listeleri
    symptoms = models.JSONField(
        default=list, 
        blank=True, 
        verbose_name="Klinik Belirtiler (Liste)",
        help_text='Köşeli parantez içinde, her madde çift tırnaklı bir metin olacak şekilde liste yazın. Örnek: ["Belirti 1", "Belirti 2"]'
    )
    favorable_conditions = models.TextField(verbose_name="Tetikleyici Çevresel Koşullar")
    case_scenario = models.TextField(verbose_name="Saha Vaka Raporu")
    
    # Organik Reçete Alanları
    organic_recipe_name = models.CharField(max_length=200, verbose_name="Organik Reçete Adı")
    organic_recipe_prep = models.TextField(verbose_name="Reçete Hazırlanışı")
    organic_recipe_app = models.TextField(verbose_name="Sahada Uygulanışı")
    preventative_measures = models.JSONField(
        default=list, 
        blank=True, 
        verbose_name="Önleyici Tedbirler (Liste)",
        help_text='Köşeli parantez içinde, her madde çift tırnaklı bir metin olacak şekilde liste yazın. Örnek: ["Önlem 1", "Önlem 2"]'
    )
    
    # Liste Görünümü Önizlemeleri
    recipe_preview = models.TextField(blank=True, null=True, verbose_name="Kısa Reçete Önizlemesi (Kartlar İçin)")
    pros = models.JSONField(
        default=list, 
        blank=True, 
        verbose_name="Avantajlar (Üretim Modelleri İçin)",
        help_text='JSON formatında başlık ve açıklama listesi. Örnek: [{"title": "Avantaj Başlığı", "desc": "Detaylı açıklama..."}]'
    )
    cons = models.JSONField(
        default=list, 
        blank=True, 
        verbose_name="Dezavantajlar (Üretim Modelleri İçin)",
        help_text='JSON formatında başlık ve açıklama listesi. Örnek: [{"title": "Dezavantaj Başlığı", "desc": "Detaylı açıklama..."}]'
    )

    class Meta:
        verbose_name = "Ziraat Rehberi İçeriği"
        verbose_name_plural = "Ziraat Rehberi İçerikleri"
        ordering = ['id']

    def __str__(self):
        return f"{self.title} ({self.season})"
