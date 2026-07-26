import os
import sys
import django

# Django ayarlarını yükle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from encyclopedia.models import Plant, Disease

# Senin eski verilerin
treatments_data = [
    (0, "Biber - Bakteriyel Leke",
     "Bakır içerikli bakterisitler uygulayın. Hastalıklı yaprakları budayın ve tarladan uzaklaştırın."),
    (1, "Biber - Sağlıklı", "Bitkiniz sağlıklı! Mevcut sulama ve gübreleme rutinine devam edin."),
    (2, "Patates - Erken Yanıklık", "Mancozeb veya Chlorothalonil bazlı fungisitler kullanın. Damlama sulamaya geçin."),
    (3, "Patates - Geç Yanıklık",
     "Acil durum! Metalaxyl içeren sistemik fungisitler uygulayın. Tarladaki nemi azaltın."),
    (4, "Patates - Sağlıklı", "Bitkiniz sağlıklı! Düzenli takibe devam edin."),
    (5, "Domates - Bakteriyel Leke", "Bakır sülfat ve Mancozeb karışımı uygulayın. Üstten sulama yapmayın."),
    (6, "Domates - Erken Yanıklık", "Alt yaprakları budayın. Azoxystrobin içerikli fungisit uygulayın."),
    (7, "Domates - Geç Yanıklık", "Hızla yayılır. Fosetil-Al veya Propamocarb bazlı ilaçlar kullanın."),
    (8, "Domates - Yaprak Küfü", "Sera havalandırmasını artırın. Difenoconazole bazlı ilaçlar kullanın."),
    (9, "Domates - Septoria Yaprak Lekesi", "Chlorothalonil fungisit uygulayın. Yabancı otları temizleyin."),
    (10, "Domates - Örümcek Akarı",
     "Abamectin veya Spiromesifen içerikli akarisitler uygulayın. Kuru ortamlarda hızla ürerler."),
    (11, "Domates - Hedef Lekesi", "Mancozeb bazlı koruyucu fungisitler kullanın. Hava sirkülasyonunu artırın."),
    (12, "Domates - Sarı Yaprak Kıvırcıklık Virüsü",
     "Tedavisi yoktur. Beyazsinek (vektör) mücadelesi yapın. Hastalıklı bitkiyi söküp yakın."),
    (13, "Domates - Mozaik Virüsü",
     "Tedavisi yoktur. Aletleri dezenfekte edin. Enfekte bitkileri imha edin. Sigara içenlerin ellerini yıkaması gerekir."),
    (14, "Domates - Sağlıklı", "Harika! Domatesleriniz gayet sağlıklı görünüyor.")
]

for class_id, full_name, treatment in treatments_data:
    # "Biber - Bakteriyel Leke" metnini "Biber" ve "Bakteriyel Leke" olarak ikiye bölüyoruz
    if " - " in full_name:
        plant_name, disease_name = full_name.split(" - ")
    else:
        plant_name = "Bilinmeyen"
        disease_name = full_name

    # Önce Bitkiyi bul veya oluştur (Biber, Patates, Domates)
    plant, created = Plant.objects.get_or_create(name=plant_name)

    # Sonra Hastalığı oluştur ve bu bitkiye bağla
    Disease.objects.update_or_create(
        ai_class_id=class_id,
        defaults={
            'plant': plant,
            'name': disease_name,
            'symptoms': 'Sistem tarafından otomatik aktarıldı. Daha sonra güncellenecek.',
            'chemical_treatment': treatment
        }
    )

print("Kral, tüm eski verilerin başarıyla yeni Django veritabanına aktarıldı!")
