# -*- coding: utf-8 -*-
import os
import sys
import django
import json
import time

# Django ortamını başlat
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from encyclopedia.models import Plant, Disease
from django.core.files.base import ContentFile
import google.generativeai as genai

# Gemini API Anahtarı ve modeli tanımlama
GEMINI_API_KEY = "AIzaSyBOWZwCsSc4yGJjuf3zLSbEugxdUA9k1Ws"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# 100 yaygın tarım bitkisinin Türkçe listesi
PLANT_LIST = [
    "Domates", "Biber", "Patates", "Çilek", "Salatalık", "Patlıcan", "Karpuz", "Kavun", 
    "Kabak", "Sarımsak", "Soğan", "Fasulye", "Nohut", "Mercimek", "Buğday", "Arpa", 
    "Yulaf", "Mısır", "Pamuk", "Ayçiçeği", "Zeytin", "İncir", "Üzüm", "Elma", 
    "Armut", "Şeftali", "Kayısı", "Erik", "Kiraz", "Vişne", "Portakal", "Mandalina", 
    "Limon", "Greyfurt", "Nar", "Ayva", "Dut", "Ceviz", "Fındık", "Antep Fıstığı", 
    "Badem", "Kestane", "Yer Fıstığı", "Susam", "Çeltik", "Çay", "Tütün", "Şeker Pancarı", 
    "Yonca", "Ispanak", "Pırasa", "Lahana", "Karnabahar", "Brokoli", "Enginar", "Kereviz", 
    "Havuç", "Turp", "Pancar", "Maydanoz", "Dereotu", "Nane", "Roka", "Tere", 
    "Marul", "Semizotu", "Pazı", "Bamya", "Fesleğen", "Reyhan", "Kekik", "Adaçayı", 
    "Biberiye", "Lavanta", "Defne", "Ihlamur", "Kuşburnu", "Kivi", "Avokado", "Muz", 
    "Trabzon Hurması", "Mango", "Ejder Meyvesi", "Hünnap", "Alıç", "Muşmula", "Kızılcık", 
    "Böğürtlen", "Ahududu", "Yaban Mersini", "Kuşkonmaz", "Brüksel Lahanası", "Bezelye", 
    "Bakla", "Rezene", "Börülce", "Karahindiba", "Zencefil", "Zerdeçal", "Keten"
]

# Görsel oluşturmak için minimalist çizim fonksiyonu
def generate_mock_image(plant_name):
    try:
        from PIL import Image, ImageDraw, ImageFont
        # Premium pastel zemin renkleri
        import hashlib
        h = hashlib.md5(plant_name.encode('utf-8')).hexdigest()
        r = int(h[0:2], 16) % 100 + 100  # 100-200 arası pastel tonlar
        g = int(h[2:4], 16) % 80 + 140   # 140-220 arası yeşilimsi/pastel
        b = int(h[4:6], 16) % 100 + 100  # 100-200 arası
        
        img = Image.new('RGB', (800, 600), color=(r, g, b))
        draw = ImageDraw.Draw(img)
        
        # Basit minimalist yaprak çizimi
        draw.ellipse([350, 200, 450, 350], fill=(46, 125, 50), outline=(27, 94, 32), width=3)
        draw.line([400, 200, 400, 380], fill=(27, 94, 32), width=4)
        draw.arc([350, 240, 450, 310], 0, 180, fill=(27, 94, 32), width=2)
        
        # Bitki adını yaz
        # Standart font olmadığı durumlar için güvenli fallback
        try:
            font = ImageFont.load_default()
        except:
            font = None
            
        draw.text((400, 450), plant_name, fill=(20, 20, 20), anchor="mm", font_size=40)
        draw.text((400, 500), "AI Ziraat Premium Kütüphanesi", fill=(60, 60, 60), anchor="mm", font_size=20)
        
        from io import BytesIO
        buf = BytesIO()
        img.save(buf, format='JPEG', quality=90)
        return buf.getvalue()
    except Exception as e:
        print(f"Görsel oluşturma hatası ({plant_name}): {str(e)}")
        return None

def fetch_data_from_gemini(plant_name):
    prompt = (
        f"Ziraat uzmanı olarak bana '{plant_name}' bitkisi için detaylı zirai kütüphane verisi üret.\n"
        f"ÇIKTI FORMATI KESİNLİKLE AŞAĞIDAKİ JSON YAPISINDA OLMALIDIR. Markdown vb. ekstra yazı yazma, doğrudan JSON döndür.\n"
        f"{{\n"
        f"  \"scientific_name\": \"Bitkinin bilimsel Latince adı\",\n"
        f"  \"description\": \"Bitki hakkında genel tanıtım, iklim ve yetiştirme koşullarını anlatan 2-3 cümlelik Türkçe bilgi.\",\n"
        f"  \"diseases\": [\n"
        f"    {{\n"
        f"      \"name\": \"Hastalık Adı 1 (Örn: Mildiyö veya Kırmızı Örümcek Zararı vb.)\",\n"
        f"      \"symptoms\": \"Hastalığın yapraklarda, meyvede ve gövdede görülen net Türkçe belirtileri.\",\n"
        f"      \"organic_treatment\": \"Zararlı veya hastalıkla mücadelede ev yapımı, biyolojik veya organik çözüm tarifleri.\",\n"
        f"      \"chemical_treatment\": \"Bitki koruma ürünleri ile yapılacak kimyasal reçete/çözüm ve ilaç tavsiyesi.\",\n"
        f"      \"prevention\": \"Hastalık ortaya çıkmadan önce alınması gereken kültürel önlemler ve sulama/bakım ipuçları.\"\n"
        f"    }},\n"
        f"    {{\n"
        f"      \"name\": \"Hastalık Adı 2\",\n"
        f"      \"symptoms\": \"Belirtiler...\",\n"
        f"      \"organic_treatment\": \"Organik çözüm...\",\n"
        f"      \"chemical_treatment\": \"Kimyasal çözüm...\",\n"
        f"      \"prevention\": \"Önlemler...\"\n"
        f"    }},\n"
        f"    {{\n"
        f"      \"name\": \"Hastalık Adı 3\",\n"
        f"      \"symptoms\": \"Belirtiler...\",\n"
        f"      \"organic_treatment\": \"Organik çözüm...\",\n"
        f"      \"chemical_treatment\": \"Kimyasal çözüm...\",\n"
        f"      \"prevention\": \"Önlemler...\"\n"
        f"    }}\n"
        f"  ]\n"
        f"}}"
    )
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            text = response.text.strip()
            # Temizle (Bazen markdown ```json ``` blokları ekliyor)
            if text.startswith("```"):
                lines = text.split("\n")
                if lines[0].startswith("```json") or lines[0].startswith("```"):
                    text = "\n".join(lines[1:-1])
            return json.loads(text.strip())
        except Exception as e:
            err_msg = str(e)
            if "429" in err_msg or "Quota exceeded" in err_msg or "ResourceExhausted" in err_msg:
                # Quota limit - sleep and retry
                sleep_time = 45
                print(f"   [!] Hiz limitine takilindi. {sleep_time} saniye bekleniyor (Deneme {attempt+1}/{max_retries})...")
                time.sleep(sleep_time)
                continue
            else:
                print(f"   [!] Gemini API hatasi ({plant_name}): {err_msg}")
                return None
    return None

def fetch_real_plant_image(plant_name):
    """Fetches high-quality real plant image URL from Wikipedia API and returns the bytes."""
    import urllib.request
    import urllib.parse
    import json
    
    # Try Turkish Wikipedia first, then English
    urls = [
        f"https://tr.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={urllib.parse.quote(plant_name)}",
        f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={urllib.parse.quote(plant_name)}"
    ]
    
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'AI-Ziraat-Bot/1.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                pages = res_data.get('query', {}).get('pages', {})
                for page_id, page_data in pages.items():
                    if 'original' in page_data:
                        img_url = page_data['original']['source']
                        # Download image
                        img_req = urllib.request.Request(img_url, headers={'User-Agent': 'AI-Ziraat-Bot/1.0'})
                        with urllib.request.urlopen(img_req, timeout=10) as img_resp:
                            return img_resp.read()
        except:
            pass
            
    return None

def get_plant_category(name):
    lower_name = name.lower()
    fruits = [
        "karpuz", "kavun", "çilek", "incir", "üzüm", "elma", "armut", "şeftali", 
        "kayısı", "erik", "kiraz", "vişne", "portakal", "mandalina", "limon", 
        "greyfurt", "nar", "ayva", "dut", "kivi", "avokado", "muz", 
        "trabzon hurması", "mango", "ejder meyvesi", "hünnap", "alıç", "muşmula", 
        "kızılcık", "böğürtlen", "ahududu", "yaban mersini", "pitaya"
    ]
    vegetables = [
        "domates", "biber", "patates", "salatalık", "patlıcan", "kabak", "sarımsak", 
        "soğan", "fasulye", "nohut", "mercimek", "ıspanak", "pırasa", "lahana", 
        "karnabahar", "brokoli", "enginar", "kereviz", "havuç", "turp", "pancar", 
        "bamya", "brüksel lahanası", "bezelye", "bakla", "kuşkonmaz"
    ]
    grains = ["buğday", "arpa", "yulaf", "mısır", "çeltik"]
    herbs = [
        "maydanoz", "dereotu", "nane", "roka", "tere", "marul", "semizotu", "pazı", 
        "fesleğen", "reyhan", "kekik", "adaçayı", "biberiye", "lavanta", "defne", 
        "ihlamur", "kuşburnu", "rezene", "börülce", "karahindiba", "zencefil", 
        "zerdeçal", "keten"
    ]
    for fruit in fruits:
        if fruit in lower_name:
            return "Meyveler"
    for veg in vegetables:
        if veg in lower_name:
            return "Sebzeler"
    for grain in grains:
        if grain in lower_name:
            return "Tahıllar"
    for herb in herbs:
        if herb in lower_name:
            return "Baharat & Otlar"
    return "Diğer"

def main():
    print("--------------------------------------------------")
    print("   AI Ziraat Otomatik Bitki Veritabani Populatoru ")
    print("--------------------------------------------------")
    print(f"Toplam hedef bitki sayisi: {len(PLANT_LIST)}")
    print("Veri cekme ve veritabanina kaydetme islemi basliyor...\n")
    
    success_count = 0
    
    for index, plant_name in enumerate(PLANT_LIST, start=1):
        print(f"[{index}/{len(PLANT_LIST)}] {plant_name} isleniyor...")
        
        # Zaten varsa atla veya güncelle
        plant_exists = Plant.objects.filter(name=plant_name).exists()
        if plant_exists:
            print(f"   -> {plant_name} veritabaninda zaten mevcut. Guncelleniyor...")
            plant = Plant.objects.get(name=plant_name)
        else:
            plant = Plant(name=plant_name)
            
        # Gemini'den verileri çek
        data = fetch_data_from_gemini(plant_name)
        if not data:
            print(f"   [!] Gemini'den veri cekilemedi ({plant_name}). 3 saniye bekleniyor ve devam ediliyor...")
            time.sleep(3)
            continue
            
        plant.scientific_name = data.get('scientific_name', '')
        plant.description = data.get('description', '')
        plant.category = get_plant_category(plant_name)
        
        # Görsel oluştur ve kaydet
        image_data = fetch_real_plant_image(plant_name)
        if image_data:
            plant.image.save(f"{plant_name.lower().replace(' ', '_')}.jpg", ContentFile(image_data), save=False)
            print(f"   [+] Resim Wikipedia Commons uzerinden indirildi: {plant_name}")
        elif not plant.image:
            image_data = generate_mock_image(plant_name)
            if image_data:
                plant.image.save(f"{plant_name.lower().replace(' ', '_')}.jpg", ContentFile(image_data), save=False)
                print(f"   [+] Fallback minimalist yaprak cizildi: {plant_name}")
                
        plant.save()
        
        # Hastalıkları ekle
        # Biber, Patates ve Domates yapay zeka sınıf hizalamaları (0-14 arası) fix_disease_class_ids.py ile yüklendiği için bunları ellemiyoruz!
        if plant_name in ["Biber", "Patates", "Domates"]:
            print(f"   [~] {plant_name} yapay zeka hizali hastaliklari korunuyor (Hastalik ekleme atlandi).")
            success_count += 1
            time.sleep(2)
            continue

        # Mevcut hastalıkları temizle ki çakışma olmasın
        plant.diseases.all().delete()
        
        diseases_data = data.get('diseases', [])
        for idx, dis in enumerate(diseases_data):
            Disease.objects.create(
                plant=plant,
                name=dis.get('name', 'Bilinmeyen Hastalik'),
                symptoms=dis.get('symptoms', 'Belirti belirtilmemis.'),
                organic_treatment=dis.get('organic_treatment', 'Organik tarif bulunmuyor.'),
                chemical_treatment=dis.get('chemical_treatment', 'Kimyasal recete bulunmuyor.'),
                prevention=dis.get('prevention', 'Kulturel onlem bulunmuyor.'),
                ai_class_id=idx + 1
            )
            
        print(f"   [+] {plant_name} kutuphaneye basariyla eklendi! ({len(diseases_data)} hastalik yuklendi)")
        success_count += 1
        
        # Gemini API Hız limiti/Sıcaklık koruması için kısa bir ara verelim
        time.sleep(2)
        
    print("\n--------------------------------------------------")
    print(f"   Basariyla {success_count}/{len(PLANT_LIST)} bitki kutuphaneye eklendi/guncellendi!")
    print("SQLite veritabanı basariyla zenginlestirildi.")
    print("--------------------------------------------------")

if __name__ == '__main__':
    main()
