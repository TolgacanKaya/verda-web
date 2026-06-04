from django.db import models
from accounts.models import FarmerProfile
from encyclopedia.models import Plant


class Post(models.Model):
    author = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='posts',
                               verbose_name="Çiftçi/Yazar")
    image = models.ImageField(upload_to='community/posts/', null=True, blank=True, verbose_name="Tarla/Yaprak Fotoğrafı")
    content = models.TextField(verbose_name="Soru veya Paylaşım")

    # Kullanıcı dilerse "Domates" veya "Biber" diye etiketleyebilir
    related_plant = models.ForeignKey(Plant, on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name="İlgili Bitki Etiketi")

    # Sorun çözüldüyse yeşil tik koymak için
    is_solved = models.BooleanField(default=False, verbose_name="Çözüme Kavuştu mu?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Paylaşım Tarihi")

    def __str__(self):
        return f"{self.author.user.username} - {self.created_at.strftime('%d %b %Y')}"

    class Meta:
        verbose_name = "Köy Meydanı Gönderisi"
        verbose_name_plural = "Köy Meydanı Gönderileri"
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="İlgili Gönderi")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name="Üst Yorum")
    author = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='comments',
                               verbose_name="Yorum Yapan")
    content = models.TextField(verbose_name="Yorum/Tavsiye")
    created_at = models.DateTimeField(auto_now_add=True)

    # Ziraat uzmanları/Adminler yorum yaparsa bu True olacak ve yeşil tikli "Uzman Tavsiyesi" rozeti alacak
    is_expert_advice = models.BooleanField(default=False, verbose_name="Uzman Tavsiyesi mi?")

    def __str__(self):
        return f"{self.author.user.username} yorumu -> Gönderi #{self.post.id}"

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
        ordering = ['created_at']


class Notification(models.Model):
    recipient = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='notifications', verbose_name="Bildirim Alıcısı")
    sender = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='sent_notifications', verbose_name="Bildirimi Gönderen")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="İlgili Gönderi")
    text = models.CharField(max_length=255, verbose_name="Bildirim Mesajı")
    is_read = models.BooleanField(default=False, verbose_name="Okundu mu?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Bildirim Tarihi")

    def __str__(self):
        return f"Bildirim: {self.recipient.user.username} <- {self.sender.user.username}"

    class Meta:
        verbose_name = "Bildirim"
        verbose_name_plural = "Bildirimler"
        ordering = ['-created_at']