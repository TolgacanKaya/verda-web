# -*- coding: utf-8 -*-
import os
import sys
import django

# Django ortamını başlat
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from encyclopedia.models import Plant, Disease

def fix_ids():
    print("---------------------------------------------------------")
    print("   AI Ziraat Çakışan Sınıf ID'lerini Temizleme Motoru   ")
    print("---------------------------------------------------------")
    
    # 1. Biber, Patates ve Domates DIŞINDAKİ tüm bitkilerin hastalıklarının ai_class_id değerlerini -1 yap
    other_diseases = Disease.objects.exclude(plant__name__in=["Biber", "Patates", "Domates"])
    count = other_diseases.count()
    other_diseases.update(ai_class_id=-1)
    print(f"[+] Yapay zeka dışı {count} adet hastalığın sınıf ID'si -1 olarak güncellendi ve çakışmalar engellendi.")

    # 2. fix_disease_class_ids.py scriptinin çalıştırılarak Biber, Patates ve Domates hastalıklarının 0-14 arası ID'lerini garanti altına al
    print("[*] Biber, Patates ve Domates hastalık hizalamaları tekrarlanıyor...")
    from fix_disease_class_ids import run_fix
    run_fix()
    
    print("[+] Çakışmalar tamamen çözüldü! Yapay zeka modeli artık biber, patates ve domatesi hatasız eşleştirecektir.")

if __name__ == '__main__':
    fix_ids()
