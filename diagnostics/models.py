from django.db import models
from accounts.models import FarmerProfile
from encyclopedia.models import Disease


class DiagnosticReport(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='reports')
    original_image = models.ImageField(upload_to='diagnostics/original/', verbose_name="Yüklenen Fotoğraf")
    heatmap_image = models.ImageField(upload_to='diagnostics/heatmaps/', blank=True, null=True,
                                      verbose_name="XAI Isı Haritası")

    # Model sonucu emin değilse veya listede yoksa diye disease null olabilir
    detected_disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name="Teşhis Edilen Hastalık")
    confidence_score = models.FloatField(verbose_name="Güven Skoru (%)")

    is_user_verified = models.BooleanField(default=False, verbose_name="Kullanıcı Doğruladı mı?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Teşhis Tarihi")

    def __str__(self):
        disease_name = self.detected_disease.name if self.detected_disease else "Bilinmiyor"
        return f"Rapor: {self.farmer.user.username} - {disease_name} (%{self.confidence_score})"

    class Meta:
        verbose_name = "Teşhis Raporu"
        verbose_name_plural = "Teşhis Raporları"


class GuestIPLimit(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="IP Adresi")
    date = models.DateField(auto_now_add=True, verbose_name="Tarih")
    tokens = models.IntegerField(default=50, verbose_name="Kalan Token")

    class Meta:
        unique_together = ('ip_address', 'date')
        verbose_name = "Misafir IP Limiti"
        verbose_name_plural = "Misafir IP Limitleri"

    def __str__(self):
        return f"IP: {self.ip_address} - Tarih: {self.date} - Token: {self.tokens}"