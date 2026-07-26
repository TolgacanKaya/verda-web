# -*- coding: utf-8 -*-
import os
import sys
import django

# Django ortamını başlat
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from encyclopedia.models import Plant, Disease

def run_fix():
    print("---------------------------------------------------------")
    print("   AI Ziraat Yapay Zeka Hastalik Siniflari Hizalama Scripti ")
    print("---------------------------------------------------------")
    
    # 1. Biber Bitkisini Al veya Oluştur
    biber, created = Plant.objects.get_or_create(
        name="Biber",
        defaults={
            "scientific_name": "Capsicum annuum",
            "description": "Patlıcangiller familyasından, ılık ve sıcak iklimleri seven, C vitamini bakımından oldukça zengin, taze veya kurutularak tüketilen tek yıllık sebze türü."
        }
    )
    print(f"[+] Biber Bitkisi Hazır (ID: {biber.id})")
    
    # Biber hastalıklarını temizle
    biber.diseases.all().delete()
    print("   -> Biber eski hastaliklari temizlendi.")
    
    # Biber hastalıklarını 15 model sınıfına göre ekle
    # Sınıf 0: Pepper__bell___Bacterial_spot
    # Sınıf 1: Pepper__bell___healthy
    
    Disease.objects.create(
        plant=biber,
        name="Bakteriyel Leke (Bacterial Spot)",
        symptoms="Yapraklarda küçük, su emmiş koyu yeşil lekeler oluşur. Zamanla bu lekeler kahverengileşir, kurur ve yapraklar dökülür. Meyvelerde çökük lekeler yapar.",
        organic_treatment="Bakır sülfat (bordo bulamacı) uygulaması organik tarımda kullanılabilir. Seralarda nem oranını düşürmek ve havalandırmayı artırmak önemlidir.",
        chemical_treatment="Bakırlı fungisitler (Bakır Oksiklorür) ve koruyucu sistemik bakterisitler kullanılabilir.",
        prevention="Sertifikalı ve temiz tohum kullanın. Ekim nöbeti uygulayın. Hastalıklı bitki kalıntılarını tarladan uzaklaştırıp imha edin.",
        ai_class_id=0
    )
    
    Disease.objects.create(
        plant=biber,
        name="Biber Sağlıklı",
        symptoms="Belirti bulunmamaktadır. Bitki tamamen sağlıklıdır. Yapraklar parlak yeşil, meyveler canlı ve gürdür.",
        organic_treatment="Düzenli kompost gübrelemesi ve dengeli sulama ile gelişim desteklenebilir.",
        chemical_treatment="Kimyasal tedaviye kesinlikle gerek yoktur.",
        prevention="Düzenli bakım, havalandırma ve dengeli sulama programına devam edin.",
        ai_class_id=1
    )
    print("   [+] Biber model hastaliklari (0, 1) yuklendi.")
    
    # 2. Patates Bitkisini Al veya Oluştur
    patates, created = Plant.objects.get_or_create(
        name="Patates",
        defaults={
            "scientific_name": "Solanum tuberosum",
            "description": "Yeraltı yumruları besin değeri yüksek nişasta içeren, tüm dünyada temel besin kaynağı olarak tüketilen, serin iklimleri seven çok yıllık otsu bitki."
        }
    )
    print(f"[+] Patates Bitkisi Hazır (ID: {patates.id})")
    
    # Patates hastalıklarını temizle
    patates.diseases.all().delete()
    print("   -> Patates eski hastaliklari temizlendi.")
    
    # Patates hastalıklarını ekle
    # Sınıf 2: Potato___Early_blight
    # Sınıf 3: Potato___Late_blight
    # Sınıf 4: Potato___healthy
    
    Disease.objects.create(
        plant=patates,
        name="Erken Yanıklık (Early Blight)",
        symptoms="Yapraklarda iç içe geçmiş halkalar (hedef tahtası benzeri) içeren koyu kahverengi lekeler oluşur. Genellikle yaşlı alt yapraklarda başlar.",
        organic_treatment="Kekik yağı, neem yağı veya ısırgan otu ekstraktı püskürtülebilir. Toprak kalitesini artırın.",
        chemical_treatment="Mancozeb, Chlorothalonil veya Pyraclostrobin etken maddeli koruyucu fungisitler tercih edilmelidir.",
        prevention="Dengeli azotlu gübreleme yapın. Bitkileri alttan damla sulama ile sulayarak yaprak ıslaklık süresini azaltın.",
        ai_class_id=2
    )
    
    Disease.objects.create(
        plant=patates,
        name="Geç Yanıklık / Mildiyö (Late Blight)",
        symptoms="Yaprak uçlarında ve kenarlarında büyük, soluk yeşil ila kahverengi su emmiş lekeler belirir. Nemli havalarda yaprağın alt yüzeyinde beyaz küf tabakası oluşur.",
        organic_treatment="Bordo bulamacı ve bakır içerikli organik solüsyonlar uygulanır. Ekim sıklığı azaltılarak rüzgar sirkülasyonu artırılmalıdır.",
        chemical_treatment="Metalaxyl, Cymoxanil veya Fluazinam etken maddeli sistemik koruyucu fungisitler.",
        prevention="Sertifikalı hastalıksız yumru kullanın. Tarlada su birikmesini önleyin. Patates yapraklarının kuru kalmasına özen gösterin.",
        ai_class_id=3
    )
    
    Disease.objects.create(
        plant=patates,
        name="Patates Sağlıklı",
        symptoms="Yapraklar lekesiz, canlı ve yeşildir. Yumrular ve bitki genel olarak sağlıklı gelişim gösterir.",
        organic_treatment="Organik maddece zengin toprak ve dengeli gübreleme gelişimini destekler.",
        chemical_treatment="Gerek yoktur.",
        prevention="Sertifikalı tohumluk kullanın ve sulama sıklığını iklim şartlarına göre ayarlayın.",
        ai_class_id=4
    )
    print("   [+] Patates model hastaliklari (2, 3, 4) yuklendi.")

    # 3. Domates Bitkisini Al veya Oluştur
    domates, created = Plant.objects.get_or_create(
        name="Domates",
        defaults={
            "scientific_name": "Solanum lycopersicum",
            "description": "Dünya genelinde en çok yetiştirilen ve tüketilen, likopen zengini kırmızı meyveleri için yetiştirilen, sıcak ve güneşli iklimleri seven tek yıllık tarım bitkisi."
        }
    )
    print(f"[+] Domates Bitkisi Hazır (ID: {domates.id})")
    
    # Domates hastalıklarını temizle
    domates.diseases.all().delete()
    print("   -> Domates eski hastaliklari temizlendi.")
    
    # Domates hastalıklarını ekle
    # Sınıf 5: Tomato_Bacterial_spot
    # Sınıf 6: Tomato_Early_blight
    # Sınıf 7: Tomato_Late_blight
    # Sınıf 8: Tomato_Leaf_Mold
    # Sınıf 9: Tomato_Septoria_leaf_spot
    # Sınıf 10: Tomato_Spider_mites_Two_spotted_spider_mite
    # Sınıf 11: Tomato__Target_Spot
    # Sınıf 12: Tomato__Tomato_YellowLeaf__Curl_Virus
    # Sınıf 13: Tomato__Tomato_mosaic_virus
    # Sınıf 14: Tomato_healthy

    Disease.objects.create(
        plant=domates,
        name="Bakteriyel Leke (Bacterial Spot)",
        symptoms="Yapraklar, saplar ve meyvelerde küçük, koyu kahverengi, pürüzlü lekeler oluşur. Meyvedeki lekeler çatlak ve siğil benzeri görünür.",
        organic_treatment="Bakır sülfat (bordo bulamacı) püskürtülebilir. Enfekte bitkileri derhal söküp tarladan uzaklaştırın.",
        chemical_treatment="Bakır bazlı fungisitler ve koruyucu bakterisitler.",
        prevention="Yağmurlama sulamadan kaçının. Temiz sertifikalı tohum ve sağlıklı fideler kullanın.",
        ai_class_id=5
    )
    
    Disease.objects.create(
        plant=domates,
        name="Erken Yanıklık (Early Blight)",
        symptoms="Yapraklarda konsantrik halkalı koyu kahverengi lekeler oluşur. Şiddetli durumlarda yapraklar sararır ve dökülür, gövdede de lekeler görülebilir.",
        organic_treatment="Bordo bulamacı uygulamaları ve hastalıklı alt yaprakların budanarak havalandırılması.",
        chemical_treatment="Difenoconazole, Tebuconazole veya Mancozeb içeren fungisitler.",
        prevention="Alt yaprakları budayarak toprakla temasını kesin. Havalandırmayı iyi tutun, seralarda nemi düşürün.",
        ai_class_id=6
    )

    Disease.objects.create(
        plant=domates,
        name="Geç Yanıklık / Mildiyö (Late Blight)",
        symptoms="Büyük kahverengi-siyah lekeler ve nemli havalarda yaprak altında beyaz küf örtüsü. Meyvede sert, pürüzlü büyük kahverengi çürümeler başlar.",
        organic_treatment="Bakırlı organik preparatlar ve enfekte alt yaprakların koruyucu budaması.",
        chemical_treatment="Propamocarb, Dimethomorph veya Metalaxyl içerikli fungisitler.",
        prevention="Sabah erken saatlerde sulama yapın. Seraları iyi havalandırın. Bitkileri sık ekmeyin.",
        ai_class_id=7
    )

    Disease.objects.create(
        plant=domates,
        name="Yaprak Küfü (Leaf Mold)",
        symptoms="Yaprakların üst yüzeyinde sarı lekeler oluşurken, alt yüzeyinde soluk zeytin yeşili kadifemsi küf tabakası gelişir. Genellikle seralarda yaygındır.",
        organic_treatment="Sera nemini %70'in altında tutun. Seralarda havalandırmayı maksimuma çıkarın.",
        chemical_treatment="Chlorothalonil veya Difenoconazole içeren fungisitler.",
        prevention="Dayanıklı çeşitler seçin. Ekim sıklığını azaltarak yapraklar arasında hava sirkülasyonunu artırın.",
        ai_class_id=8
    )

    Disease.objects.create(
        plant=domates,
        name="Septoria Yaprak Lekesi (Septoria Leaf Spot)",
        symptoms="Yapraklarda kenarları koyu kahverengi, merkezleri gri-beyaz olan küçük, yuvarlak lekeler oluşur. Lekelerin merkezinde siyah noktacıklar (piknid) görülür.",
        organic_treatment="Bordo bulamacı püskürtülmesi. Toprak yüzeyine malç sererek patojenin yağmur sularıyla sıçramasını önleme.",
        chemical_treatment="Chlorothalonil, Mancozeb veya Azoxystrobin bazlı fungisitler.",
        prevention="Bitkileri sırığa alarak yaprakların toprakla temasını engelleyin. Sulamayı doğrudan köklere yapın.",
        ai_class_id=9
    )

    Disease.objects.create(
        plant=domates,
        name="İki Noktalı Kırmızı Örümcek (Spider Mites)",
        symptoms="Yaprakların üst yüzeyinde ince beyaz/sarı noktacıklar oluşur. Yaprakların alt kısımlarında çok ince ipeksi ağlar gözlenir. Bitki solgunlaşır ve kurur.",
        organic_treatment="Neem yağı (azadirachtin), kükürt uygulaması veya arap sabunlu solüsyonlar püskürtün. Doğal avcı akarları koruyun.",
        chemical_treatment="Abamectin, Spirodiclofen veya Hexythiazox etken maddeli spesifik akarisitler.",
        prevention="Tozlu ortamları azaltın (toz kırmızı örümcek artışını tetikler). Nemi dengeli tutun.",
        ai_class_id=10
    )

    Disease.objects.create(
        plant=domates,
        name="Hedef Leke (Target Spot)",
        symptoms="Yapraklarda iç içe geçmiş halkalar içeren, soluk yeşilden açık kahverengiye değişen hedef tahtası benzeri yuvarlak lekeler. Meyvelerde de çökük siyah lekeler yapar.",
        organic_treatment="Bordo bulamacı ve bitki özlü organik koruyucu yağlar püskürtülmesi.",
        chemical_treatment="Boscalid, Pyraclostrobin veya Azoxystrobin içeren fungisitler.",
        prevention="Sera nemini kontrol edin, yabancı ot temizliğine özen gösterin ve alt yaprakları budayın.",
        ai_class_id=11
    )

    Disease.objects.create(
        plant=domates,
        name="Sarı Yaprak Kıvırcıklık Virüsü (Yellow Leaf Curl Virus)",
        symptoms="Yapraklar yukarı doğru kase şeklinde kıvrılır, küçülür ve belirgin şekilde sararır. Bitkide cüceleşme ve çiçek dökülmesi görülür. Beyazsinekler tarafından taşınır.",
        organic_treatment="Beyazsineklerle mücadele için sarı yapışkan tuzaklar kullanın. Enfekte bitkileri hemen söküp yakın.",
        chemical_treatment="Virüse doğrudan kimyasal ilaç yoktur. Vektör beyazsinekler için Acetamiprid veya Imidacloprid içeren insektisitler kullanılır.",
        prevention="Beyazsineklere karşı tül/ağ kullanın. Dayanıklı hibrid tohumlar tercih edin.",
        ai_class_id=12
    )

    Disease.objects.create(
        plant=domates,
        name="Mozaik Virüsü (Mosaic Virus)",
        symptoms="Yapraklarda açık ve koyu yeşil renk dalgalanmaları (mozaik deseni), kıvrılmalar ve şekil bozuklukları oluşur. Meyvelerde kahverengi nekrozlar görülebilir.",
        organic_treatment="Doğrudan organik tedavisi yoktur. Aletleri %10'luk çamaşır suyu solüsyonu ile dezenfekte edin.",
        chemical_treatment="Doğrudan kimyasal tedavisi yoktur. Enfekte bitkiler derhal sökülüp yok edilmelidir.",
        prevention="Tohumları ekimden önce sodyum fosfat ile dezenfekte edin. Çalışanların ellerini ve aletlerini sık sayfada yıkamasını sağlayın.",
        ai_class_id=13
    )

    Disease.objects.create(
        plant=domates,
        name="Domates Sağlıklı",
        symptoms="Yapraklar parlak yeşil, meyveler dolgun, canlı ve pürüzsüzdür. Bitkide hiçbir hastalık belirtisi yoktur.",
        organic_treatment="Doğal solucan gübresi ve düzenli damla sulama ile bitki gelişimi desteklenebilir.",
        chemical_treatment="Gerek yoktur.",
        prevention="Düzenli kontroller ve dengeli gübreleme-sulama rejimine devam edin.",
        ai_class_id=14
    )
    print("   [+] Domates model hastaliklari (5, 6, 7, 8, 9, 10, 11, 12, 13, 14) yuklendi.")
    print("---------------------------------------------------------")
    print("   Yapay Zeka Hastalik Siniflari Basariyla Duzenlendi! ")
    print("---------------------------------------------------------")

if __name__ == '__main__':
    run_fix()
