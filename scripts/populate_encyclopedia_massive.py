import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from encyclopedia.models import Plant

PLANTS = [
    # SEBZELER
    ("Domates", "Solanum lycopersicum", "Sebzeler", "Antioksidan deposu, yemeklerin vazgeçilmezi olan yaygın bir sera ve tarla bitkisi."),
    ("Biber", "Capsicum annuum", "Sebzeler", "Tatlı, acı, dolmalık gibi pek çok çeşidi bulunan C vitamini açısından çok zengin bir sebze."),
    ("Patlıcan", "Solanum melongena", "Sebzeler", "Sıcak iklimleri seven, mor renkli meyveleriyle bilinen lezzetli bir yaz sebzesi."),
    ("Salatalık", "Cucumis sativus", "Sebzeler", "Yüksek su içeriği ile serinletici, hem açıkta hem serada yetiştirilen tırmanıcı bir bitki."),
    ("Kabak", "Cucurbita pepo", "Sebzeler", "Hızlı büyüyen, hem meyvesi hem de çekirdeği için yetiştirilebilen yazlık bir sebze."),
    ("Kavun", "Cucumis melo", "Sebzeler", "Sıcak yaz aylarının vazgeçilmezi, tatlı, sulu ve aromatik meyveli sürünücü bir bitki."),
    ("Karpuz", "Citrullus lanatus", "Sebzeler", "Yaz aylarında serinlemek için bolca tüketilen, çok su isteyen geniş alan bitkisi."),
    ("Fasulye", "Phaseolus vulgaris", "Sebzeler", "Hem taze (yeşil) hem de kuru olarak tüketilen, toprağa azot bağlayan faydalı bir baklagil sebzesi."),
    ("Bezelye", "Pisum sativum", "Sebzeler", "Serin iklimleri seven, ilkbahar ve sonbaharda yetiştirilebilen tatlı taneli bir bitki."),
    ("Bamya", "Abelmoschus esculentus", "Sebzeler", "Sıcağa ve kurağa oldukça dayanıklı, mukilajlı yapısıyla bilinen yaz sebzesi."),
    ("Ispanak", "Spinacia oleracea", "Sebzeler", "Demir ve vitamin açısından zengin, kısa günlerde ve serin havalarda iyi gelişen yapraklı sebze."),
    ("Lahana", "Brassica oleracea var. capitata", "Sebzeler", "Serin iklim kış sebzesi olup, çok katmanlı kalın yapraklarıyla bilinir."),
    ("Karnabahar", "Brassica oleracea var. botrytis", "Sebzeler", "Çiçek tomurcukları tüketilen, serin iklim koşullarında yüksek verim veren kışlık sebze."),
    ("Brokoli", "Brassica oleracea var. italica", "Sebzeler", "Kanser önleyici bileşenler içeren, yeşil çiçek taslakları yenen besleyici bir bitki."),
    ("Pırasa", "Allium ampeloprasum", "Sebzeler", "Soğangillerden, gövdesi tüketilen, kış aylarında dona oldukça dayanıklı bir bitki."),
    ("Kuru Soğan", "Allium cepa", "Sebzeler", "Mutfakların temel taşı olan, uzun raf ömrü ve keskin aromasıyla bilinen yumrulu bitki."),
    ("Sarımsak", "Allium sativum", "Sebzeler", "Doğal antibiyotik olarak anılan, dişler halinde büyüyen mucizevi bir allium türü."),
    ("Havuç", "Daucus carota", "Sebzeler", "A vitamini ve beta-karoten deposu olan, serin topraklarda iyi gelişen kök sebzesi."),
    ("Turp", "Raphanus sativus", "Sebzeler", "Çok hızlı hasada gelen, acımtırak tadıyla bilinen kışlık kök sebze."),
    ("Şalgam", "Brassica rapa subsp. rapa", "Sebzeler", "Özellikle suyu için kullanılan, soğuğa dayanıklı bir kök bitkisi."),
    ("Kereviz", "Apium graveolens", "Sebzeler", "Hem yaprakları hem de kök yumrusu tüketilen, kendine has aroması olan sonbahar sebzesi."),
    ("Enginar", "Cynara cardunculus", "Sebzeler", "Karaciğer dostu olarak bilinen, Ege ve Akdeniz iklimini seven çok yıllık devedikeni türü."),
    ("Marul", "Lactuca sativa", "Sebzeler", "Salataların vazgeçilmezi, kısa sürede hasada gelen, serin iklim yapraklı sebzesi."),
    ("Maydanoz", "Petroselinum crispum", "Sebzeler", "Türk mutfağında çokça kullanılan, C vitamini zengini kokulu otsu bitki."),
    ("Dereotu", "Anethum graveolens", "Sebzeler", "Özellikle zeytinyağlı yemeklerde kullanılan, ince tüysü yapraklı aromatik bitki."),
    ("Roka", "Eruca vesicaria", "Sebzeler", "Keskin ve baharatlı tadıyla balık sofralarının favorisi olan hızlı büyüyen yeşillik."),
    ("Tere", "Lepidium sativum", "Sebzeler", "Su kenarlarını seven, acımtırak ve ferahlatıcı tadıyla bilinen küçük yapraklı bitki."),
    ("Semizotu", "Portulaca oleracea", "Sebzeler", "Omega-3 açısından çok zengin, sulu yapraklı ve toprakta yayılarak büyüyen yaz otu."),
    ("Pazı", "Beta vulgaris var. cicla", "Sebzeler", "Ispanağa benzeyen ancak daha geniş yapraklı ve iri damarlı olan bir kış sebzesi."),
    ("Kuşkonmaz", "Asparagus officinalis", "Sebzeler", "Tohumdan hasada uzun yıllar süren, pahalı ve çok lezzetli sürgünler veren çok yıllık bitki."),
    ("Bakla", "Vicia faba", "Sebzeler", "Baharın müjdecisi olan, azot sabitleyici özelliği ile toprağı zenginleştiren baklagil."),

    # MEYVELER
    ("Elma", "Malus domestica", "Meyveler", "Ilıman iklimlerin en çok yetiştirilen, uzun süre depolanabilen dayanıklı meyvesi."),
    ("Armut", "Pyrus communis", "Meyveler", "Elmaya göre daha sulu ve yumuşak dokulu, tatlı ve lifli bir ılıman iklim meyvesi."),
    ("Ayva", "Cydonia oblonga", "Meyveler", "Sarı renkli, tüylü, sert dokulu ve mayhoş tatlı, reçeli ve tatlısı yapılan sonbahar meyvesi."),
    ("Şeftali", "Prunus persica", "Meyveler", "Kadifemsi tüylü kabuğu ve tatlı sulu etiyle yaz aylarının favori meyvesi."),
    ("Kayısı", "Prunus armeniaca", "Meyveler", "Sarı-turuncu renkli, kurutularak da çok tüketilen, ilkbahar geç donlarına hassas bir meyve."),
    ("Nektarin", "Prunus persica var. nucipersica", "Meyveler", "Şeftalinin tüysüz, parlak kabuklu ve daha sıkı etli doğal mutasyonu."),
    ("Erik", "Prunus domestica", "Meyveler", "Yeşil can erikten mürdüm eriğine kadar çok çeşidi olan, ağacı dayanıklı sert çekirdekli meyve."),
    ("Kiraz", "Prunus avium", "Meyveler", "Yazın ilk müjdecisi olan, kırmızı/bordo renkli tatlı ve saplı meyveler veren ağaç."),
    ("Vişne", "Prunus cerasus", "Meyveler", "Kiraza benzeyen fakat mayhoş ve asitli tadıyla meyve suyu yapımında kullanılan tür."),
    ("Kızılcık", "Cornus mas", "Meyveler", "Kırmızı renkli, oldukça mayhoş, C vitamini zengini şifalı bir orman meyvesi."),
    ("İncir", "Ficus carica", "Meyveler", "Sıcak iklimleri seven, sütünün ve kurusunun faydaları saymakla bitmeyen lezzetli meyve."),
    ("Üzüm", "Vitis vinifera", "Meyveler", "Asma bitkisinde salkım halinde yetişen, sofralık, kurutmalık ve şıralık olarak kullanılan efsanevi meyve."),
    ("Nar", "Punica granatum", "Meyveler", "Kalın kabuğunun altında yüzlerce yakut rengi tanesi olan, kuraklığa dayanıklı Akdeniz meyvesi."),
    ("Dut", "Morus", "Meyveler", "Beyaz, kara veya kırmızı renklerde, ipek böcekçiliğinde de kullanılan çok hızlı büyüyen ağaç meyvesi."),
    ("Kivi", "Actinidia deliciosa", "Meyveler", "Sarmaşık formunda büyüyen, nemli iklimleri (özellikle Karadeniz) seven C vitamini deposu."),
    ("Trabzon Hurması", "Diospyros kaki", "Meyveler", "Cennet hurması olarak da bilinen, sonbahar sonunda olgunlaşan turuncu renkli tatlı meyve."),
    ("Portakal", "Citrus sinensis", "Meyveler", "Kış aylarının C vitamini kaynağı, parlak turuncu renkli narenciye türü."),
    ("Mandalina", "Citrus reticulata", "Meyveler", "Portakala göre daha küçük, kabuğu kolay soyulan, hoş kokulu narenciye."),
    ("Limon", "Citrus limon", "Meyveler", "Yüksek asiditesiyle yemeklere, salatalara lezzet veren, dona karşı en hassas narenciye."),
    ("Greyfurt", "Citrus paradisi", "Meyveler", "Mayhoş ve hafif acımtırak tadıyla bilinen, metabolizmayı hızlandıran iri narenciye."),
    ("Çilek", "Fragaria × ananassa", "Meyveler", "Kırmızı, sulu ve tatlı, toprak yüzeyine yakın yetişen otsu orman meyvesi."),
    ("Ahududu", "Rubus idaeus", "Meyveler", "Frambuaz olarak da bilinir, çok lezzetli, çalı formunda yetişen hassas bir meyve."),
    ("Böğürtlen", "Rubus fruticosus", "Meyveler", "Dikenli çalılarda salkımlar halinde yetişen, siyahlaştıkça tatlanan orman meyvesi."),
    ("Yaban Mersini", "Vaccinium myrtillus", "Meyveler", "Asidik toprakları seven, mavi/mor renkli, antioksidan bakımından şampiyon olan meyve."),
    ("Badem", "Prunus dulcis", "Meyveler", "İlkbaharda en erken çiçek açan, sert kabuklu içi yenilen oldukça besleyici kuruyemiş."),
    ("Ceviz", "Juglans regia", "Meyveler", "Beyin gelişimine faydalı omega yağ asitleri içeren, görkemli ve büyük ağaçların meyvesi."),
    ("Fındık", "Corylus avellana", "Meyveler", "Karadeniz iklimini seven, ocak formunda dikilen çalımsı ağaççıkların lezzetli meyvesi."),
    ("Kestane", "Castanea sativa", "Meyveler", "Kış aylarında közde pişirilen, yüksek nişasta oranına sahip dağ meyvesi."),
    ("Antep Fıstığı", "Pistacia vera", "Meyveler", "Güneydoğu anadolu iklimini seven, kuraklığa çok dayanıklı, altın değerinde kuruyemiş."),
    ("Zeytin", "Olea europaea", "Meyveler", "Ölmez ağacı olarak bilinen, Akdeniz efsanesi, yağı ve meyvesiyle insanlığın en büyük dostu."),

    # TAHILLAR
    ("Buğday", "Triticum", "Tahıllar", "Dünya nüfusunun temel besin kaynağı olan, un ve ekmek yapımında kullanılan tahıl."),
    ("Arpa", "Hordeum vulgare", "Tahıllar", "Hayvan yemi ve malt yapımında kullanılan, soğuğa dayanıklı, kısa sürede yetişen tahıl."),
    ("Yulaf", "Avena sativa", "Tahıllar", "Lif oranı çok yüksek, atların favorisi olan ve kahvaltılık ezme yapılan sağlıklı tahıl."),
    ("Çavdar", "Secale cereale", "Tahıllar", "Toprak seçiciliği en az olan, soğuğa en dayanıklı, esmer ekmek yapımında kullanılan tahıl."),
    ("Mısır", "Zea mays", "Tahıllar", "Sıcak ve bol su isteyen, hem insan hem hayvan beslenmesinde kritik olan iri taneli tahıl."),
    ("Çeltik (Pirinç)", "Oryza sativa", "Tahıllar", "Bol su içinde, tavalarda yetiştirilen, Asya'nın temel besini olan tahıl."),
    ("Darı", "Panicum miliaceum", "Tahıllar", "Kuraklığa dayanıklı, kuş yemi veya boza yapımında kullanılan küçük taneli tahıl."),
    ("Karabuğday", "Fagopyrum esculentum", "Tahıllar", "Glutensiz olmasıyla öne çıkan, aslında tahıl olmayan fakat tahıl gibi tüketilen bir bitki."),
    ("Tritikale", "Triticosecale", "Tahıllar", "Buğday ile çavdarın melezlenmesiyle elde edilen, yüksek verimli ve dayanıklı yem bitkisi."),

    # BAHARAT & OTLAR
    ("Kekik", "Thymus vulgaris", "Baharat & Otlar", "Kuru ve taşlık arazileri seven, aromatik yağ oranı yüksek şifalı ve lezzetli bitki."),
    ("Fesleğen", "Ocimum basilicum", "Baharat & Otlar", "Hoş kokulu, Akdeniz ve İtalyan mutfağında sıkça kullanılan narin yapraklı yaz otu."),
    ("Biberiye", "Rosmarinus officinalis", "Baharat & Otlar", "Herdemyeşil, çam iğnesine benzer yaprakları olan çok güçlü antioksidan bir çalı."),
    ("Adaçayı", "Salvia officinalis", "Baharat & Otlar", "Gümüşi yeşil yaprakları olan, kışın çayı yapılarak içilen boğaz dostu bitki."),
    ("Lavanta", "Lavandula", "Baharat & Otlar", "Mor çiçekleri ve rahatlatıcı eşsiz kokusuyla parfümeri ve peyzaj alanında popüler çalı."),
    ("Melisa", "Melissa officinalis", "Baharat & Otlar", "Limon kokulu, sakinleştirici etkisiyle bilinen, çayı çok sevilen oğul otu."),
    ("Papatya", "Matricaria chamomilla", "Baharat & Otlar", "Kırların beyaz çiçeği, kurutulup çay yapıldığında uykusuzluğa ve strese iyi gelen bitki."),
    ("Rezene", "Foeniculum vulgare", "Baharat & Otlar", "Anason benzeri kokuya sahip, sindirimi rahatlatan uzun boylu sarı çiçekli ot."),
    ("Kimyon", "Cuminum cyminum", "Baharat & Otlar", "Tohumları baharat olarak kullanılan, et yemeklerine eşsiz lezzet katan kurak iklim bitkisi."),
    ("Anason", "Pimpinella anisum", "Baharat & Otlar", "Kendine has yoğun kokusuyla, hamur işlerinde ve geleneksel içkilerde kullanılan bitki."),
    ("Kişniş", "Coriandrum sativum", "Baharat & Otlar", "Hem yaprakları (silantro) hem de tohumları kullanılan baharatlı ot."),
    ("Sumak", "Rhus coriaria", "Baharat & Otlar", "Kırmızı, ekşimsi meyveleri toz haline getirilerek kebap ve salatalara dökülen çalı."),
    ("Defne", "Laurus nobilis", "Baharat & Otlar", "Herdemyeşil yaprakları yemeklere koku vermek için kullanılan Akdeniz ağacı."),
    ("Nane", "Mentha", "Baharat & Otlar", "Mentol içeren, ferahlatıcı, sulak yerleri çok seven yayılıcı kokulu ot."),

    # DİĞER (Endüstriyel & Baklagiller)
    ("Pamuk", "Gossypium", "Diğer", "Dokuma sanayinin beyaz altını, sıcağı seven ve kozasındaki lifler için ekilen endüstri bitkisi."),
    ("Tütün", "Nicotiana tabacum", "Diğer", "Yaprakları için yetiştirilen, çok fazla el işçiliği gerektiren önemli bir endüstri bitkisi."),
    ("Şeker Pancarı", "Beta vulgaris", "Diğer", "Köklerindeki yüksek sakaroz oranıyla şeker üretiminde kullanılan serin iklim bitkisi."),
    ("Ayçiçeği", "Helianthus annuus", "Diğer", "Güneşe dönük büyük sarı tablaları olan, sıvı yağ üretiminde dünyada ilk sıralardaki bitki."),
    ("Soya Fasulyesi", "Glycine max", "Diğer", "Protein oranı en yüksek bitki olup, hem yağ hem yem sanayisinde vazgeçilmezdir."),
    ("Yer Fıstığı", "Arachis hypogaea", "Diğer", "Çiçekleri döllendikten sonra toprağa girerek meyvesini toprak altında büyüten ilginç bir bitki."),
    ("Susam", "Sesamum indicum", "Diğer", "Sıcak iklimleri seven, tahin ve simit üretiminde kullanılan yüksek yağ oranlı bitki."),
    ("Haşhaş", "Papaver somniferum", "Diğer", "Devlet kontrolünde ekilen, gıda, yağ ve ilaç (alkaloid) sanayisinde kullanılan bitki."),
    ("Aspir", "Carthamus tinctorius", "Diğer", "Kuraklığa çok dayanıklı, yalancı safran olarak da bilinen dikenli bir yağ bitkisi."),
    ("Kanola", "Brassica napus", "Diğer", "Sarı çiçek tarlalarıyla görsel şölen sunan, biyodizel ve yemeklik yağ üretiminde kullanılan bitki."),
    ("Nohut", "Cicer arietinum", "Diğer", "Kurağa en dayanıklı baklagillerden, leblebi yapımından humus yapımına geniş kullanım alanı olan bitki."),
    ("Mercimek", "Lens culinaris", "Diğer", "Kırmızı, yeşil, sarı renkleri olan, kışlık ve yazlık ekilebilen zengin protein kaynağı baklagil."),
    ("Kuru Fasulye", "Phaseolus vulgaris", "Diğer", "Türk mutfağının baş tacı, protein açısından çok zengin bir tarla baklagili."),
    ("Çay", "Camellia sinensis", "Diğer", "Türkiye'de sadece Doğu Karadeniz'de yetişen, yaprakları fermente edilerek içilen çok yıllık çalı."),
    ("Keten", "Linum usitatissimum", "Diğer", "Hem liflerinden tekstil yapılan hem de tohumundan omega zengini keten tohumu yağı elde edilen bitki.")
]

def run():
    print(f"Toplam {len(PLANTS)} adet bitki verisi hazırlanıyor...")
    count = 0
    updated = 0
    for name, sci, cat, desc in PLANTS:
        plant, created = Plant.objects.get_or_create(
            name=name,
            defaults={
                'scientific_name': sci,
                'category': cat,
                'description': desc
            }
        )
        if created:
            count += 1
            print(f"Eklendi: {name}")
        else:
            # Sadece kategorisini veya tanımını güncelle
            if plant.category == 'Diğer' and cat != 'Diğer' or not plant.description:
                plant.category = cat
                plant.description = desc
                plant.scientific_name = sci
                plant.save()
                updated += 1
                print(f"Güncellendi: {name}")
            else:
                pass # Zaten mevcut
                
    print(f"\n--- İŞLEM TAMAMLANDI ---")
    print(f"Yeni eklenen bitki sayısı: {count}")
    print(f"Güncellenen bitki sayısı: {updated}")
    print("Ansiklopedi veritabanı 100+ bitki ile zenginleştirildi!")

if __name__ == "__main__":
    run()
