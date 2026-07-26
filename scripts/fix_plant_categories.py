# -*- coding: utf-8 -*-
import os
import sys
import django

# Django ortamını başlat
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from encyclopedia.models import Plant

def get_plant_category(name):
    lower_name = name.toLowerCase() if hasattr(name, 'toLowerCase') else name.lower()
    
    # Meyveler
    fruits = [
        "karpuz", "kavun", "çilek", "incir", "üzüm", "elma", "armut", "şeftali", 
        "kayısı", "erik", "kiraz", "vişne", "portakal", "mandalina", "limon", 
        "greyfurt", "nar", "ayva", "dut", "kivi", "avokado", "muz", 
        "trabzon hurması", "mango", "ejder meyvesi", "hünnap", "alıç", "muşmula", 
        "kızılcık", "böğürtlen", "ahududu", "yaban mersini", "pitaya"
    ]
    
    # Sebzeler
    vegetables = [
        "domates", "biber", "patates", "salatalık", "patlıcan", "kabak", "sarımsak", 
        "soğan", "fasulye", "nohut", "mercimek", "ıspanak", "pırasa", "lahana", 
        "karnabahar", "brokoli", "enginar", "kereviz", "havuç", "turp", "pancar", 
        "bamya", "brüksel lahanası", "bezelye", "bakla", "kuşkonmaz"
    ]
    
    # Tahıllar
    grains = ["buğday", "arpa", "yulaf", "mısır", "çeltik"]
    
    # Yeşillikler / Baharat & Otlar
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
    print("---------------------------------------------------------")
    print("   AI Ziraat Mevcut Bitki Kategorilerini Onarma Scripti ")
    print("---------------------------------------------------------")
    
    plants = Plant.objects.all()
    updated_count = 0
    
    for plant in plants:
        category = get_plant_category(plant.name)
        plant.category = category
        plant.save()
        print(f"[+] Bitki: {plant.name} -> Kategori: {category}")
        updated_count += 1
        
    print("---------------------------------------------------------")
    print(f"   Muvaffakiyetle {updated_count} bitki kategorize edildi! ")
    print("---------------------------------------------------------")

if __name__ == '__main__':
    main()
