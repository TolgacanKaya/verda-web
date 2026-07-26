import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from field_guide.models import FieldGuideItem

ALL_SEED_ITEMS = [
    # İLKBAHAR MEVSİMİ (14 Orijinal Öğe)
    {
        'slug': 'kirmizi-orumcek-salgini',
        'title': 'Kırmızı Örümcek Akarı İstilası',
        'scientific_name': 'Tetranychus urticae',
        'category': 'Zararlı İstilası',
        'season': 'İlkbahar',
        'risk_level': 'Yüksek',
        'description': 'Bahar aylarında havaların ısınmasıyla yaprak altlarında ağlar örerek özsuyu emen, yapraklarda sarı noktalar ve sonrasında kuruma oluşturan mikroskobik akarlardır.',
        'symptoms': [
            'Yaprak üst yüzeyinde ince gümüşi-sarı noktacıklar oluşmesi',
            'Yaprak altlarında çok ince örümcek ağlarının gözlenmesi',
            'Şiddetli zarar durumunda yaprakların kahverengileşip dökülmesi'
        ],
        'favorable_conditions': '20-25°C sıcaklık, %50 altındaki düşük nem ve rüzgarsız kuru hava.',
        'case_scenario': 'Nisan ayı sonlarında sera içi nemin aniden düşmesiyle birlikte patlıcan ve fasulye yapraklarının rengi solmaya başlar. Yaprakların arkasını inceleyen üretici, milimetrik hareket eden kırmızı noktaları ve yoğun ağ tabakasını fark eder. Zamanında müdahale edilmediğinde bitkiler fotosentez yeteneğini kaybederek 1 hafta içinde kurur.',
        'organic_recipe_name': 'Kekik Yağı ve Isırgan Otu Ekstratı',
        'organic_recipe_prep': '10 litre suya 30 ml saf soğuk pres kekik yağı, 50 ml sıvı arap sabunu ve 24 saat fermente edilmiş ısırgan otu suyu eklenerek emülsiyon oluşturulur.',
        'organic_recipe_app': 'Rüzgarsız ve güneşsiz akşamüstü saatlerinde, yaprak altları tamamen ıslanacak şekilde sisleme şeklinde püskürtülür. 5 gün arayla 3 kez tekrarlanır.',
        'preventative_measures': [
            'Arazi içi ve çevresindeki kuru yabancı otlar temizlenmelidir.',
            'Damlama sulama ile toprak nemli tutulmalı ve kuraklık stresi önlenmelidir.',
            'Doğal avcı akar (Phytoseiulus persimilis) popülasyonları desteklenmelidir.'
        ],
        'recipe_preview': 'Nem seviyesi yüksek tutulmalı, kekik yağı ve arap sabunu karışımlı solüsyon rüzgarsız akşamüstleri yaprak altlarına sislenerek uygulanmalıdır.'
    },
    {
        'slug': 'bakteriyel-solgunluk-ralstonia',
        'title': 'Bakteriyel Solgunluk Hastalığı',
        'scientific_name': 'Ralstonia solanacearum',
        'category': 'Bakteri Girişi',
        'season': 'İlkbahar',
        'risk_level': 'Çok Yüksek',
        'description': 'Toprak kökenli bakterilerin kök yaralarından sızarak bitkinin su iletim borularını tıkaması sonucu yapraklarda sararma olmadan bitkinin aniden yeşilken solup ölmesidir.',
        'symptoms': [
            'Gündüz saatlerinde yapraklarda sararma olmadan aniden solma',
            'Akşam saatlerinde solgunluğun geçici olarak düzelmesi',
            'Gövde kesildiğinde iletim demetlerinin kahverengileşmesi ve suya batırıldığında bakteriyel akıntı çıkması'
        ],
        'favorable_conditions': '22-28°C yüksek toprak sıcaklıkları ve aşırı toprak nemi, drenajsız araziler.',
        'case_scenario': 'Mayıs ayında domates tarlasında çapalama esnasında kökler hafif zarar görür. Ardından gelen aşırı yağışlar toprağı çamurlaştırır. Birkaç gün sonra sağlıklı görünen bitkiler sararmadan yeşil halde aniden solar. Kesilen gövdeden çıkan yapışkan akıntı bakteriyel solgunluğu doğrular ve tarla karantinaya alınır.',
        'organic_recipe_name': 'Kireç Kaymağı ve Kekik Esansı Aşılaması',
        'organic_recipe_prep': 'Kök bölgesine uygulanmak üzere toprağın pH dengesini ayarlayacak sönmüş kireç bulamacı hazırlanır. Sulama suyuna bakteri karşıtı kekik ve karabaş otu yağları eklenir.',
        'organic_recipe_app': 'Hastalıklı bitki söküldükten sonra ocak kireçlenir. Çevredeki sağlıklı bitkilerin kök bölgesine şerbet halinde uygulanarak bakterinin yayılımı sınırlandırılır.',
        'preventative_measures': [
            'Budama ve çapalama aletleri her kullanımda dezenfekte edilmelidir.',
            'Toprak pH seviyesi kireçleme ile 7.0-7.2 arasında dengelenmelidir.',
            'Aşırı sulamadan kaçınılmalı, arazide göllenme önlenmelidir.'
        ],
        'recipe_preview': 'Hastalıklı bitki anında sökülüp ocak kireçlenmeli, sağlıklı bitki köklerine koruyucu olarak kireçli ve kekik yağlı şerbet verilmelidir.'
    },
    {
        'slug': 'kul-leme-biber',
        'title': 'Biberde Yaprak Külleme Hastalığı',
        'scientific_name': 'Leveillula taurica',
        'category': 'Fungus Yayılımı',
        'season': 'İlkbahar',
        'risk_level': 'Orta-Yüksek',
        'description': 'Genellikle biber yapraklarının alt yüzeyinde başlayan, beyaz unsu mantar tabakası ve üst yüzeyde sarı lekelerle karakterize fungal hastalıktır.',
        'symptoms': [
            'Yaprakların üst yüzeyinde düzensiz sarı lekeler',
            'Yaprak alt yüzeyinde unsu, beyaz küf tabakası',
            'Zamanla yaprakların kıvrılması, kuruması ve dökülmesi'
        ],
        'favorable_conditions': '18-24°C sıcaklık, nemli geceler (%80) ve kuru gündüzler (%40), havasız dikim aralıkları.',
        'case_scenario': 'Nisan ayı sonunda biber serasında havalandırmanın yetersiz olduğu kör noktalardaki bitkilerde sararmalar başlar. Yaprakların arkası çevrildiğinde un serpilmiş gibi beyaz bir tabaka görülür. Hızla yayılan külleme mantarı, çiçeklerin dökülmesine ve hasat veriminin %40 azalmasına neden olur.',
        'organic_recipe_name': 'Sodyum Bikarbonat ve Neem Koruyucu',
        'organic_recipe_prep': '10 litre suya 50 gram sodyum bikarbonat (kabartma tozu), 30 ml arap sabunu ve 20 ml organik neem yağı karıştırılır.',
        'organic_recipe_app': 'Yapraklara hem alt hem üst yüzeyi kaplayacak şekilde püskürtülür. Sabah erken saatlerde uygulanması önerilir. 7 gün arayla tekrarlanır.',
        'preventative_measures': [
            'Sera içi nem sirkülasyon fanlarıyla kontrol altında tutulmalıdır.',
            'Alt yapraklar budanarak bitki gövdesinin rüzgar alması sağlanmalıdır.',
            'Aşırı azotlu gübrelemeden kaçınılarak bitki dokularının gevşek büyümesi önlenmelidir.'
        ],
        'recipe_preview': 'Sodyum bikarbonat ve neem yağı karışımı sabah serinliğinde tüm yapraklara püskürtülmeli, hava sirkülasyonu artırılmalıdır.'
    },
    {
        'slug': 'domates-lekeli-solgunluk',
        'title': 'Domates Lekeli Solgunluk Virüsü (TSWV)',
        'scientific_name': 'Tomato Spotted Wilt Virus',
        'category': 'Virüs Hastalığı',
        'season': 'İlkbahar',
        'risk_level': 'Çok Yüksek',
        'description': 'Thrips adı verilen böcekler aracılığıyla taşınan, yapraklarda bronzlaşma, halkalı lekeler ve bitki büyümesinde cüceleşme oluşturan tedavisi olmayan virüstür.',
        'symptoms': [
            'Genç yapraklarda bronzlaşma ve morumsu renk değişimi',
            'Yaprak ve meyve yüzeyinde iç içe geçmiş kahverengi halkalı lekeler',
            'Sürgün uçlarında kuruma, geriye doğru ölüm ve bitki boyunun kısa kalması'
        ],
        'favorable_conditions': 'Thrips popülasyonunun yüksek olduğu kuru ve sıcak ilkbahar günleri, yabancı ot kontrolü zayıf tarlalar.',
        'case_scenario': 'Mayıs başında biber ve domates tarlalarında thrips popülasyonu artar. Birkaç hafta sonra domates bitkilerinin tepe yapraklarında morarma ve cüceleşme başlar. Yapraklarda halkalı lekeler belirir. Virüs sistemik olarak bitkiyi sardığı için verim sıfırlanır ve bitkiler sökülmek zorunda kalır.',
        'organic_recipe_name': 'Mavi Tuzak ve Sarımsak Thrips Savar',
        'organic_recipe_prep': 'Thrips mücadelesi için 10 litre suya 5 baş sarımsak maseratı, 30 ml arap sabunu ve 10 ml kekik yağı eklenerek karıştırılır.',
        'organic_recipe_app': 'Virüsün tedavisi yoktur. Ancak taşıyıcı thripsleri engellemek için hazırlanan böcek kaçırıcı solüsyon haftada bir kez bitkilere püskürtülür. Tarlaya yoğun şekilde mavi ve sarı yapışkan tuzaklar asılır.',
        'preventative_measures': [
            'Mavi yapışkan tuzaklar thripsleri yakalamak için dikimle birlikte asılmalıdır.',
            'Tarla çevresindeki virüs taşıyıcısı yabancı otlar temizlenmelidir.',
            'Böcek tüllerinden (insect net) faydalanarak seraya thrips girişi engellenmelidir.'
        ],
        'recipe_preview': 'Virüsün tedavisi yoktur; mavi yapışkan tuzaklar asılarak ve sarımsak bazlı böcek kaçırıcı solüsyonlarla thrips taşıyıcıları engellenmelidir.'
    },
    {
        'slug': 'salatalik-mozaik-virusu',
        'title': 'Salatalık Mozaik Virüsü (CMV)',
        'scientific_name': 'Cucumber Mosaic Virus',
        'category': 'Virüs Hastalığı',
        'season': 'İlkbahar',
        'risk_level': 'Yüksek',
        'description': 'Yaprak bitleri (afitler) aracılığıyla taşınan, salatalık ve kabak yapraklarında mozaik benzeri sarı-yeşil lekeler ve meyvelerde şekil bozuklukları oluşturan viral enfeksiyondur.',
        'symptoms': [
            'Yapraklarda açık ve koyu yeşil renklerin oluşturduğu mozaik deseni',
            'Yaprak boyutunda küçülme ve kenarlarında aşağı doğru kıvrılma',
            'Meyvelerde pürüzlü, siğilli yapı ve belirgin renk bozulmaları'
        ],
        'favorable_conditions': 'Yaprak bitlerinin hızla çoğaldığı 15-22°C ılıman ilkbahar dönemleri.',
        'case_scenario': 'İlkbahar ekimi yapılan salatalıklarda havaların ısınmasıyla yaprak bitleri görülür. Afitlerin beslenmesinin ardından salatalık yapraklarında koyu yeşil büzüşmeler ve kabarcıklı mozaik lekeleri başlar. Bitkiler gelişemez, toplanan salatalıklar ise yamuk yumruk ve sert pürüzlü hale gelir.',
        'organic_recipe_name': 'Süt Proteini ve Afit Engelleyici Neem',
        'organic_recipe_prep': '10 litre suya 1.5 litre yağsız süt and 30 ml neem yağı eklenerek homojen hale gelene kadar karıştırılır.',
        'organic_recipe_app': 'Yağsız süt virüsün mekanik yayılımını engellemek amacıyla budama öncesinde bitkilere püskürtülür. Neem yağı ise yaprak bitlerini kaçırmak için yaprak altlarına uygulanır.',
        'preventative_measures': [
            'Aletler her bitkiden sonra %10\'luk çamaşır suyu veya alkolle sterilize edilmelidir.',
            'Tarladaki enfekte bitkiler sökülüp yakılmalıdır, komposta atılmamalıdır.',
            'Yaprak biti taşıyıcılarına karşı koruyucu sarı tuzaklar yerleştirilmelidir.'
        ],
        'recipe_preview': 'Enfekte bitkiler imha edilmeli, yaprak bitlerini uzak tutmak için neem yağı püskürtülmeli ve budama aletleri sürekli sterilize edilmelidir.'
    },
    {
        'slug': 'fide-kok-curuklugu-rhizoctonia',
        'title': 'Fide Kök ve Kök Boğazı Çürüklüğü',
        'scientific_name': 'Rhizoctonia solani',
        'category': 'Toprak Mantarı',
        'season': 'İlkbahar',
        'risk_level': 'Yüksek',
        'description': 'İlkbaharda ekilen fidelerin toprak altındaki kök ve kök boğazı dokularını çürütüp bitkinin beslenmesini engelleyen ve kurumasına yol açan toprak kökenli fungal patojendir.',
        'symptoms': [
            'Köklerde kahverengi-siyah renk değişimi ve doku dökülmesi',
            'Kök boğazında çökük, kırmızımsı kahverengi kuru lezyonlar',
            'Bitkinin gelişemeyip cüce kalması, yaprakların sararıp kuruması'
        ],
        'favorable_conditions': '15-20°C serin toprak sıcaklığı, yüksek nem ve ağır yapılı, hava almayan killi topraklar.',
        'case_scenario': 'Mart ayında ağır killi toprağa dikilen fide kökleri soğuk ve ıslak toprakta boğulur. Rhizoctonia mantarı zayıflayan köklere saldırarak çürütür. Fideler dikildikten sonra hiç büyüyemez, yaprak uçlarından başlayarak sararır ve hafifçe çekildiğinde köksüz olarak topraktan kolayca ayrılır.',
        'organic_recipe_name': 'Bacillus ve Hümik Asit Kök Aşısı',
        'organic_recipe_prep': '10 filtre suya 40 gram Bacillus subtilis (faydalı bakteri) ve 50 ml sıvı hümik asit eklenerek karıştırılır.',
        'organic_recipe_app': 'Fide dikim çukuruna can suyu olarak uygulanır. Dikimden 10 gün sonra damlama sulama ile kök bölgesine tekrarlanır.',
        'preventative_measures': [
            'Dikim öncesi toprağa bol kompost karıştırılarak havalanma artırılmalıdır.',
            'Soğuk topraklarda ekim yapılmamalı, toprak sıcaklığının 15°C üzerine çıkması beklenmelidir.',
            'Aşırı sulamadan kaçınılmalı, malçlama ile toprak nem dengesi korunmalıdır.'
        ],
        'recipe_preview': 'Toprak sıcaklığı uygun seviyeye gelmeden ekim yapılmamalı, kök bölgesine Bacillus subtilis bakterileri can suyu ile aşılanmalıdır.'
    },
    {
        'slug': 'yaprak-galerisinegi-istilasi',
        'title': 'Yaprak Galeri Sineği Zararı',
        'scientific_name': 'Liriomyza spp.',
        'category': 'Zararlı İstilası',
        'season': 'İlkbahar',
        'risk_level': 'Orta',
        'description': 'Sinek larvalarının yaprak iki çeperi arasına girerek tüneller (galeriler) açması ve fotosentez alanını daraltarak bitkiyi zayıflatması durumudur.',
        'symptoms': [
            'Yaprak yüzeyinde beyaz, yılan gibi kıvrımlı ince tünel izleri',
            'Yapraklarda delikler ve sineğin beslenme noktalarında küçük sarı benekler',
            'Yoğun bulaşmalarda yaprağın tamamen kuruyup dökülmesi'
        ],
        'favorable_conditions': '20-25°C sıcaklık ve orta derecede bağıl nemli bahar günleri, yabancı ot kontrolsüzlüğü.',
        'case_scenario': 'Nisan ayında fasulye ve kabak yapraklarında garip beyaz çizgiler belirir. Gün geçtikçe bu çizgiler yılan gibi kıvrılarak yaprağın tamamını sarar. Larvalar yaprak içinde beslendikçe yaprak kurur. Fotosentez yapamayan bitki çiçek dökerek meyve bağlayamaz.',
        'organic_recipe_name': 'Sarı Yapışkan Levha ve Spinosad Çözeltisi',
        'organic_recipe_prep': '10 litre suya 5 ml Spinosad (doğal bakteri fermantasyon ürünü) ve 10 ml organik yayıcı eklenir.',
        'organic_recipe_app': 'Sinek uçuşunu engellemek için bitki boyuna sarı yapışkan tuzaklar asılır. Hazırlanan Spinosad solüsyonu, yapraklarda ilk galeriler görüldüğünde akşamüstü püskürtülür.',
        'preventative_measures': [
            'Tarladaki yabancı otlar sineğe konukçuluk ettiği için düzenli temizlenmelidir.',
            'Hasat sonrasında tarladaki bitki artıkları derin sürümle toprağa gömülmelidir.',
            'Zararlı sinek larvalarını yiyen parazitoit avcı böcekler korunmalıdır.'
        ],
        'recipe_preview': 'Sarı yapışkan tuzaklar asılmalı, yapraklarda tünel izleri görüldüğünde doğal Spinosad içeren solüsyonla ilaçarama yapılmalıdır.'
    },
    {
        'slug': 'biberde-fitoftora-curuklugu',
        'title': 'Biberde Fitoftora Kök Çürüklüğü',
        'scientific_name': 'Phytophthora capsici',
        'category': 'Toprak Mantarı',
        'season': 'İlkbahar',
        'risk_level': 'Çok Yüksek',
        'description': 'İlkbahar yağışları sonrasında göllenen sularda hızla yayılan sporların biber kök ve gövdesinde siyah lekeler açarak bitkiyi hızla öldürdüğü tehlikeli fungal hastalıktır.',
        'symptoms': [
            'Kök boğazında koyu kahverengi veya simsiyah renk değişimi',
            'Yapraklarda aniden pörsüme ve kuruma, bitkinin ayaktayken ölmesi',
            'Meyvelerde sulu, beyaz küflü geniş lekeler oluşması'
        ],
        'favorable_conditions': '25-28°C yüksek sıcaklık, göllenen durgun sular, ağır killi ve drenajı bozuk toprak yapısı.',
        'case_scenario': 'Mayıs ayında biber tarlasını salma sulama ile aşırı sulayan çiftçi, suyun tarlanın alt kısmında göllenmesine neden olur. Göllenen suda Phytophthora sporları hızla çoğalarak biber gövdelerini kök boğazından sarar. 3 gün içinde tarlanın o bölgesindeki tüm biberler simsiyah kesilerek aniden kurur.',
        'organic_recipe_name': 'Bakır Oktaonat ve Trichoderma Kök Kalkanı',
        'organic_recipe_prep': '10 filtre suya 25 gram bakır oktaonat (organik bakır tuzu) ve 50 gram Trichoderma harzianum eklenir.',
        'organic_recipe_app': 'Can suyu veya damlama sulama ile doğrudan kök bölgesine uygulanır. Göllenen alanlardaki hastalıklı bitkiler sökülüp çevresi ilaçlanır.',
        'preventative_measures': [
            'Biber dikimleri kesinlikle karık usulü sırtlara (yükseltilmiş yataklara) yapılmalıdır.',
            'Salma sulamadan kesinlikle kaçınılmalı, su birikmesi engellenmelidir.',
            'Münavebe uygulanarak patlıcan, domates ve biber ardı ardına ekilmemelidir.'
        ],
        'recipe_preview': 'Salma sulama yapılmamalı, dikimler sırtlara yapılmalı ve köklere koruyucu olarak faydalı mantarlar (Trichoderma) aşılanmalıdır.'
    },
    {
        'slug': 'domates-paspas-akari',
        'title': 'Domates Pas Akarı Hasarı',
        'scientific_name': 'Aculops lycopersici',
        'category': 'Zararlı İstilası',
        'season': 'İlkbahar',  # Orijinal ilkbahar öğesi
        'risk_level': 'Yüksek',
        'description': 'Bahar sonu ve yaz başlarında domates gövde ve yapraklarında beslenerek bitkiye paslı, bronz bir görünüm veren ve yaprakların çıtırdayıp kurumasına sebep olan mikroskobik akarlardır.',
        'symptoms': [
            'Gövde ve yaprakların alt kısımlarından başlayan pas rengi, bronzlaşma',
            'Yaprakların kağıt gibi kuruyup çıtırlaşması ve kenarlarından büzülmesi',
            'Meyve kabuğunda sertleşme, çatlaklar ve mat paslı görünüm'
        ],
        'favorable_conditions': '26-32°C yüksek sıcaklıklar, kuraklık stresi ve düşük bağıl nem.',
        'case_scenario': 'Sera içi havanın ısınmasıyla birlikte bitkilerin alt gövdeleri kahverengileşmeye başlar. Üretici bunun mantar olduğunu düşünüp fungisit atar ancak etki etmez. Gövde bronzlaşarak yukarı tırmanır, yapraklar kurur. Pas akarları tüm serayı sarar.',
        'organic_recipe_name': 'Islanabilir Kükürt ve Neem Yağı Kokteyli',
        'organic_recipe_prep': '10 litre suya 40 gram ıslanabilir kükürt ve 25 ml soğuk pres neem yağı eklenerek iyice karıştırılır.',
        'organic_recipe_app': 'Güneşin yakıcı olmadığı akşam serinliğinde bitkinin alt gövdelerinden başlanarak tüm yeşil aksamına püskürtülür.',
        'preventative_measures': [
            'Bahar aylarında bitkinin susuzluk stresi yaşaması engellenmelidir.',
            'Alt yapraklar budanarak pas akarının yukarı tırmanma yolu kesilmelidir.',
            'Bulaşık bitki artıkları hasat sonrası tarladan uzaklaştırılıp imha edilmelidir.'
        ],
        'recipe_preview': 'Islanabilir kükürt ve neem yağı akşamüstü saatlerinde püskürtülmeli, bitki kuraklık stresine sokulmamalıdır.'
    },
    {
        'slug': 'ispanak-mildiyosu-fungus',
        'title': 'Ispanak Mildiyösü Hastalığı',
        'scientific_name': 'Peronospora farinosa f. sp. spinaciae',
        'category': 'Fungus Yayılımı',
        'season': 'İlkbahar',
        'risk_level': 'Yüksek',
        'description': 'İlkbaharda ıspanak yapraklarında sararma ve alt kısımlarında morumsu gri küf tabakası oluşturarak ıspanakları yenilemez hale getiren fungal hastalıktır.',
        'symptoms': [
            'Yaprakların üst yüzeyinde mat, soluk sarı lekeler oluşması',
            'Yaprak alt yüzeyinde menekşe-gri renkte yoğun tüylü mantar tabakası',
            'Yaprakların etlenip kıvrılması ve çürüyerek kuruması'
        ],
        'favorable_conditions': '8-15°C serin bahar sıcaklıkları, %90 üzeri aşırı nem ve çiğ düşmesi, sık dikilmiş tarlalar.',
        'case_scenario': 'Mart ayında sık ekilmiş ıspanak tarlasında sabahları çiğ eksik olmaz. Ispanak yapraklarında sararmalar başlar. Yaprakların altına bakıldığında morumsu gri küfler fark edilir. Hasat edilemeden çürürler.',
        'organic_recipe_name': 'Bakır Hidroksit ve Karbonat Bariyeri',
        'organic_recipe_prep': '10 litre suya 20 gram bakır hidroksit ve 30 gram sodyum bikarbonat eklenerek karıştırılır.',
        'organic_recipe_app': 'İlkbahar başlangıcında çiğ düşme dönemlerinde koruyucu olarak yapraklara püskürtülür. Yağışlardan sonra uygulama tekrarlanmalıdır.',
        'preventative_measures': [
            'Ispanak ekimi çok sık yapılmamalı, sıralar arası mesafe havalanmaya uygun olmalıdır.',
            'Damlama sulama tercih edilerek yaprakların ıslak kalma süresi azaltılmalıdır.',
            'Dayanıklı ıspanak çeşitleri tercih edilerek ekim planlanmalıdır.'
        ],
        'recipe_preview': 'Sık ekimden kaçınılmalı, çiğ düşen serin günlerde koruyucu bakır hidroksit ve karbonat karışımı yapraklara püskürtülmelidir.'
    },
    {
        'slug': 'marul-iri-damar-virusu',
        'title': 'Marul İri Damar Hastalığı',
        'scientific_name': 'Lettuce Big Vein Virus',
        'category': 'Virüs Hastalığı',
        'season': 'İlkbahar',
        'risk_level': 'Orta',
        'description': 'Toprak mantarları aracılığıyla marul köklerine bulaşan, yaprak damarlarının aşırı kalınlaşması ve bitkinin göbek bağlayamamasıyla sonuçlanan virüstür.',
        'symptoms': [
            'Yaprak damarlarının şeffaflaşması, genişlemesi ve kalınlaşması',
            'Yaprak kenarlarında dalgalanma, kırışma ve marulun göbek yapamaması',
            'Bitkinin genel olarak cüceleşmesi ve gevşek yapılı kalması'
        ],
        'favorable_conditions': '10-18°C serin toprak sıcaklıkları ve aşırı ıslak, drenajı zayıf toprak yapıları.',
        'case_scenario': 'Bahar aylarında dikilen marulların yaprakları normal formunu kaybederek damarları aşırı belirginleşir. Marullar göbek bağlayıp sertleşmek yerine gevşek ve cüce kalır.',
        'organic_recipe_name': 'Mantar Baskılayıcı Bakteri Aşısı',
        'organic_recipe_prep': 'Toprakta mantarı engellemek için 10 litre suya 50 gram Bacillus subtilis ve 50 ml neem yağı karıştırılır.',
        'organic_recipe_app': 'Ekim öncesinde veya dikim can suyuyla birlikte toprak kök bölgesine bolca dökülür. Toprak drenajı iyileştirilir.',
        'preventative_measures': [
            'Toprağın su tutması önlenmeli, drenaj kanalları açık tutulmalıdır.',
            'Dayanıklı marul çeşitleri tercih edilmeli ve ekim nöbeti yapılmalıdır.',
            'Toprak pH seviyesi kireç uygulamalarıyla dengelenmelidir.'
        ],
        'recipe_preview': 'Virüsün tedavisi yoktur; su birikimi önlenmeli ve taşıyıcı mantarı baskılamak için kök bölgesine Bacillus subtilis uygulanmalıdır.'
    },
    {
        'slug': 'cilek-kok-kurdu-larva',
        'title': 'Çilek Kök Kurdu Zararı',
        'scientific_name': 'Anthonomus signatus',
        'category': 'Zararlı İstilası',
        'season': 'İlkbahar',
        'risk_level': 'Yüksek',
        'description': 'Çilek köklerinde beslenen kınkanatlı larvalarının kökleri kesmesi sonucu çileklerin aniden kuruyarak ölmesi durumudur.',
        'symptoms': [
            'Çilek yapraklarında aniden kırmızılaşma, pörsüme ve kuruma',
            'Meyve boyutunun çok küçük kalması veya meyvelerinin olgunlaşmadan kuruması',
            'Bitki çekildiğinde köklerin tamamen kesilmiş veya çürümüş olduğunun görülmesi'
        ],
        'favorable_conditions': '15-22°C ılıman toprak sıcaklıkları, yüksek organik madde içeren nemli çilek tarhları.',
        'case_scenario': 'Nisan ayında çilek tarlasında bazı ocaklar aniden kurumaya başlar. Çiftçi sulama yapar ama çilekler kurtulamaz. Kuruyan ocak söküldüğünde toprak altında kınkanatlı larvaları görülür.',
        'organic_recipe_name': 'Entomopatojen Nematod Aşısı',
        'organic_recipe_prep': 'Kök kurtlarını biyolojik olarak yok etmek amacıyla Steinernema carpocapsae (faydalı nematod) suda çözündürülür.',
        'organic_recipe_app': 'Bulutlu günlerde veya akşam saatlerinde damlama sulama sistemi vasıtasıyla doğrudan çilek kök bölgesine verilir.',
        'preventative_measures': [
            'Ekim öncesinde toprak derin sürülerek larvalar kuşlara yem edilmelidir.',
            'Bahçede çilek aralarına böcek kaçırıcı kadife çiçeği veya sarımsak dikilmelidir.',
            'Malçlama altına giren böcekleri engellemek için tarhlar temiz tutulmalıdır.'
        ],
        'recipe_preview': 'Kök bölgesine faydalı nematodlar (Steinernema) aşılanarak toprak altındaki kurtlar biyolojik olarak temizlenmelidir.'
    },
    {
        'slug': 'biberde-kalsiyum-noksanligi',
        'title': 'Biberde Kalsiyum Noksanlığı',
        'scientific_name': 'Fizyolojik Kalsiyum Eksikliği',
        'category': 'Fizyolojik Denge',
        'season': 'İlkbahar',
        'risk_level': 'Orta',
        'description': 'Bahar sonuna doğru yükselen sıcaklıklar ve düzensiz sulama yüzünden kalsiyum mineralinin genç meyve uçlarına taşınamamasıyla biber uçlarında siyah çürük alanlar oluşmasıdır.',
        'symptoms': [
            'Biber meyvelerinin uç kısımlarında sulu lezyonlar belirmesi',
            'Meyve uçlarının kuruyup siyahlaşarak içe doğru çökmesi',
            'Yaprak uçlarında kıvrılma ve büyüme noktalarında duraksama'
        ],
        'favorable_conditions': 'Sıcak ilkbahar günleri, rüzgarlı kuru havalar, düzensiz sulama rejimi.',
        'case_scenario': 'Mayıs ayında biberler ilk meyvelerini verir. Ancak sulamada aksama yaşayan biber bitkilerinde kalsiyum taşınamaz. Biber meyvelerinin uç kısımları simsiyah olup çürür.',
        'organic_recipe_name': 'Yumurta Kabuğu Sirkesi ve Aminoasit Kalsiyum',
        'organic_recipe_prep': 'Kalsiyum kaynağı olarak fermente yumurta kabukları sirkede çözündürülür veya organik kalsiyum solüsyonu hazırlanır.',
        'organic_recipe_app': 'Biberler çiçek açıp meyve bağlamaya başladığı andan itibaren 10 gün arayla doğrudan meyvelere ve genç sürgünlere püskürtülür.',
        'preventative_measures': [
            'Damlama sulama rejimi nem sensörleri ile izlenerek düzenli tutulmalıdır.',
            'Aşırı amonyum azotu gübrelemesinden kaçınılmalıdır.',
            'Toprağın organik madde oranı kompost ilavesiyle artırılmalıdır.'
        ],
        'recipe_preview': 'Düzensiz sulamadan kaçınılmalı, çiçeklenmeden itibaren yapraktan organik kalsiyum uygulaması yapılmalıdır.'
    },
    {
        'slug': 'bakteriyel-benek-domates',
        'title': 'Domates Bakteriyel Benek Hastalığı',
        'scientific_name': 'Pseudomonas syringae pv. tomato',
        'category': 'Bakteri Girişi',
        'season': 'İlkbahar',
        'risk_level': 'Yüksek',
        'description': 'Serin ve yağışlı ilkbahar günlerinde domates yapraklarında siyah benekler ve meyvelerde çirkin siğilimsi lekeler açan bakteriyel hastalıktır.',
        'symptoms': [
            'Yapraklarda etrafı dar sarı haleyle çevrili küçük koyu kahverengi-siyah lekeler',
            'Lekelerin birleşmesiyle yaprakların kuruması ve dökülmesi',
            'Meyvelerde küçük, siyah, hafif kabarık siğilimsi beneklerin oluşması'
        ],
        'favorable_conditions': '15-22°C serin ve yağışlı ilkbahar günleri, yaprakların uzun süre ıslak kalması.',
        'case_scenario': 'Nisan ayında günlerce süren ilkbahar yağmurları domates tarlasını vurur. Yağışın hemen ardından domateslerin alt yapraklarında siyah benekler yayılmaya başlar. Budama sırasında işçilerin elleriyle tüm tarlaya bulaşır.',
        'organic_recipe_name': 'Bakır Hidroksit ve Defne Yağı Kalkanı',
        'organic_recipe_prep': '10 litre suya 20 gram bakır hidroksit ve antibakteriyel etki için 10 ml saf defne yaprağı yağı karıştırılır.',
        'organic_recipe_app': 'Yağmurlu periyotların hemen ardından veya budama işlemlerinden sonra taze olarak yapraklara püskürtülür.',
        'preventative_measures': [
            'Yağışlı havalarda ve yapraklar ıslakken kesinlikle budama ve çapa yapılmalıdır.',
            'Sertifikalı ve temiz domates tohumları kullanılmalıdır.',
            'Bitkiler arasında hava akışını artırmak için geniş dikim aralıkları bırakılmalıdır.'
        ],
        'recipe_preview': 'Yağış sonrası ve budama ardından koruyucu bakır hidroksit ve defne yağı püskürtülmeli, ıslakken budama yapılmamalıdır.'
    },

    # YAZ MEVSİMİ (6 Öğe)
    {
        'slug': 'karpuz-antraknozu-yaz',
        'title': 'Karpuz Antraknozu Hastalığı',
        'scientific_name': 'Colletotrichum orbiculare',
        'category': 'Fungus Yayılımı',
        'season': 'Yaz',
        'risk_level': 'Çok Yüksek',
        'description': 'Sıcak ve nemli yaz aylarında karpuz yapraklarında siyah lekeler, meyvelerde ise çökük dairesel yaralar açarak ürünü tamamen çürüten fungal bir enfeksiyondur.',
        'symptoms': [
            'Yapraklarda önce küçük sarımsı lekeler, zamanla büyüyerek siyahlaşan kurumalar',
            'Meyve yüzeyinde suyla ıslanmış gibi çökük, dairesel lezyonlar',
            'Nemli havalarda meyve yaralarında pembe renkli spor kitlelerinin oluşumu'
        ],
        'favorable_conditions': '22-27°C sıcaklık ve %80 üzeri bağıl nem, aşırı yağmurlama sulama.',
        'case_scenario': 'Temmuz ayında aşırı sıcaklardan dolayı yağmurlama sulamayı artıran üretici, karpuz meyvelerinin üzerinde siyah, çökük yaralar görür. Hızla yayılan antraknoz, tüm meyveleri sararak tarladaki hasadın %60 oranında fire vermesine yol açar.',
        'organic_recipe_name': 'Sarımsak Yağı ve Bakır Sülfat Emülsiyonu',
        'organic_recipe_prep': '10 litre suya 50 ml süzülmüş sarımsak yağı, 20 gram bakır sülfat (göztaşı) ve 30 ml sıvı arap sabunu karıştırılarak hazırlanır.',
        'organic_recipe_app': 'Yapraklar ve özellikle meyveler tamamen ıslanacak şekilde akşamüstü serinliğinde püskürtülür. 7 gün arayla tekrarlanır.',
        'preventative_measures': [
            'Damlama sulama sistemi tercih edilerek yapraklar kuru tutulmalıdır.',
            'Hasat sonrası tarladaki bitki artıkları yakılmalı veya derin sürümle gömülmelidir.',
            'Münavebe uygulanarak kavun-karpuz ardışık ekilmemelidir.'
        ],
        'recipe_preview': 'Yağmurlama sulamadan kaçınılmalı, bakır sülfat ve sarımsak yağı karışımı akşamüstü serinliğinde meyvelere püskürtülmelidir.'
    },
    {
        'slug': 'yesil-kurt-yaz',
        'title': 'Domateste Yeşil Kurt Hasarı',
        'scientific_name': 'Helicoverpa armigera',
        'category': 'Zararlı İstilası',
        'season': 'Yaz',
        'risk_level': 'Yüksek',
        'description': 'Yaz aylarında domates meyvelerinin içini delerek beslenen, meyveleri çürüten ve pazar değerini tamamen yok eden tehlikeli bir tırtıl zararlısıdır.',
        'symptoms': [
            'Meyve yüzeyinde düzgün, yuvarlak deliklerin bulunması',
            'Meyve içine girmiş tırtılların beslenmesi ve dışkı bırakması',
            'Zarar gören meyvelerin ikincil bakteriyel enfeksiyonlarla hızla çürümesi'
        ],
        'favorable_conditions': '25-30°C sıcaklıklar, yabancı ot kontrolü zayıf araziler.',
        'case_scenario': 'Ağustos ayında hasada hazırlanan domates tarlasında, bazı domateslerde delikler fark edilir. İçleri açıldığında yeşil-kahverengi tırtıllar görülür. Yeşil kurtlar hızla diğer salkımlara geçerek meyveleri yenemez hale getirir.',
        'organic_recipe_name': 'Bacillus thuringiensis ve Neem Çözeltisi',
        'organic_recipe_prep': '10 litre suya 30 gram Bacillus thuringiensis (Bt) preparatı ve 25 ml neem yağı karıştırılır.',
        'organic_recipe_app': 'Akşam saatlerinde tırtılların en aktif olduğu dönemde yapraklara ve meyvelere püskürtülür. Bt bakterisi tırtılın sindirim sistemini felç eder.',
        'preventative_measures': [
            'İlkbaharda derin toprak sürümü yapılarak topraktaki pupalar yok edilmelidir.',
            'Yabancı ot mücadelesi zamanında yapılmalı, konukçuluk önlenmelidir.',
            'Zararlı kelebeklerin yumurtalarını yiyen Trichogramma avcı arıcıkları korunmalıdır.'
        ],
        'recipe_preview': 'Meyvelerde delik gözlendiğinde, kelebek yumurtaları açılmadan Bacillus thuringiensis bakterisi akşam saatlerinde püskürtülmelidir.'
    },
    {
        'slug': 'yaprak-biti-yaz',
        'title': 'Yaprak Biti İstilası',
        'scientific_name': 'Aphis gossypii',
        'category': 'Zararlı İstilası',
        'season': 'Yaz',
        'risk_level': 'Orta',
        'description': 'Bitkilerin genç sürgün ve yaprak altlarında koloniler halinde yaşayarak özsuyu emen, yaprakları büzen ve fumajine yol açan emici böceklerdir.',
        'symptoms': [
            'Yaprakların kenarlarından aşağı doğru kıvrılması ve büzülmesi',
            'Bitki yüzeyinde yapışkan tatlımsı bir sıvının (balımsı madde) birikmesi',
            'Bu sıvının üzerinde siyah füme mantar tabakasının (fumajin) oluşması'
        ],
        'favorable_conditions': '20-26°C ılıman ve az esintili yaz günleri, aşırı azotlu gübreleme.',
        'case_scenario': 'Haziran ayında biber ve patlıcanların tepe sürgünleri büzüşmeye başlar. Dikkatli bakıldığında yaprak arkalarında binlerce yeşil-siyah bit görülür. Bitlerin salgıladığı yapışkan sıvı yüzünden yapraklar kararır ve fotosentez durur.',
        'organic_recipe_name': 'Arap Sabunu ve Sirkeli Doğal İnsektisit',
        'organic_recipe_prep': '10 litre suya 100 ml sıvı arap sabunu, 50 ml elma sirkesi ve 1 baş ezilmiş sarımsak eklenerek karıştırılır ve süzülür.',
        'organic_recipe_app': 'Yaprak altlarına tazyikli bir şekilde püskürtülerek böceklerin fiziksel olarak dökülmesi ve havasız kalarak ölmesi sağlanır.',
        'preventative_measures': [
            'Aşırı azotlu gübrelemeden kaçınılarak bitkinin taze sürgün vermesi dengelenmelidir.',
            'Uğur böceği (Coccinella septempunctata) ve sirfid larvaları gibi doğal avcılar desteklenmelidir.',
            'Sarı yapışkan tuzaklar bitki boyuna asılarak popülasyon izlenmelidir.'
        ],
        'recipe_preview': 'Arap sabunu, sirke ve sarımsak karışımı yaprak altlarına tazyikli püskürtülmeli, uğur böceği popülasyonu korunmalıdır.'
    },
    {
        'slug': 'domates-mildiyosu-yaz',
        'title': 'Domates Mildiyösü (Geç Yanıklık)',
        'scientific_name': 'Phytophthora infestans',
        'category': 'Fungus Yayılımı',
        'season': 'Yaz',
        'risk_level': 'Çok Yüksek',
        'description': 'Serin geçen yaz geceleri ve nemli günlerde domates yapraklarında haşlanmış gibi lekeler açan, gövdeyi karartıp bitkiyi kurutan tahrip edici fungal hastalıktır.',
        'symptoms': [
            'Yapraklarda büyük, düzensiz, önce soluk yeşil, sonra kahverengileşen lekeler',
            'Yaprak altındaki lekelerin etrafında beyaz küf tabakasının belirmesi',
            'Gövdede kararma ve meyvelerde sert, kahverengi büyük çürüklerin oluşması'
        ],
        'favorable_conditions': '16-22°C gece-gündüz sıcaklıkları, %90 üzeri bağıl nem ve çiğ düşmesi.',
        'case_scenario': 'Haziran sonundaki yağmurlu ve serin günlerin ardından domates serasında yapraklar haşlanmış gibi solar. 2 gün içinde gövdelere yayılan simsiyah lekeler bitkileri kurutur ve domatesler toplanmadan çürür.',
        'organic_recipe_name': 'Kekik Yağı ve Karbonatlı Mantar Savar',
        'organic_recipe_prep': '10 litre suya 30 ml saf kekik yağı, 40 gram sodyum bikarbonat and 30 ml arap sabunu karıştırılır.',
        'organic_recipe_app': 'Hastalık belirtileri görülmeden önce veya ilk lekelemede koruyucu olarak tüm bitkiye uygulanır. Yağış sonrası yenilenir.',
        'preventative_measures': [
            'Fideler havalanmaya imkan verecek şekilde geniş aralıklarla dikilmelidir.',
            'Damlama sulama kullanılmalı, sulama sabah erken saatlerde yapılmalıdır.',
            'Sera içi nem fanlar ve havalandırma pencereleriyle düşürülmelidir.'
        ],
        'recipe_preview': 'Serin ve nemli yaz günlerinde koruyucu olarak kekik yağı ve karbonat karışımı püskürtülmeli, havalandırma artırılmalıdır.'
    },
    {
        'slug': 'demir-noksanligi-yaz',
        'title': 'Sebzelerde Demir Noksanlığı',
        'scientific_name': 'Fizyolojik Demir Eksikliği',
        'category': 'Fizyolojik Denge',
        'season': 'Yaz',
        'risk_level': 'Orta',
        'description': 'Yüksek toprak pH seviyeleri ve kireçli topraklarda demir mineralinin alınamaması sonucu bitkinin tepe yapraklarında damar aralarının sararması durumudur.',
        'symptoms': [
            'Genç tepe yapraklarında damarların yeşil kalırken damar aralarının sararması (kloroz)',
            'Şiddetli eksiklikte yaprakların tamamen beyaza dönmesi ve kenarlarının kuruması',
            'Bitki gelişiminin durması ve çiçek dökümünün artması'
        ],
        'favorable_conditions': 'Toprak pH seviyesinin 7.5 üzerinde olması, aşırı kireçli topraklar ve soğuk/ıslak toprak şartları.',
        'case_scenario': 'Temmuz ayında yüksek kireçli tarlaya dikilen domates ve biberlerin tepe sürgünleri limon sarısına döner. Bitkiler büyümeyi durdurur. pH seviyesi yüksek olduğu için toprakta demir olsa bile bitki bunu bünyesine alamaz.',
        'organic_recipe_name': 'Limon Tuzu ve Demir Sülfat Şerbeti',
        'organic_recipe_prep': '10 litre suya 20 gram demir sülfat (saç kıbrısı) and pH düşürmek için 10 gram limon tuzu karıştırılır.',
        'organic_recipe_app': 'Güneşsiz akşamüstü saatlerinde doğrudan sararan genç yapraklara yaprak gübresi şeklinde püskürtülür. 10 gün arayla 2 kez tekrarlanır.',
        'preventative_measures': [
            'Toprağa bol miktarda kükürt uygulanarak pH seviyesi 6.0-6.8 arasına düşürülmelidir.',
            'Toprak organik maddesi iyi fermente olmuş ahır gübresi ile zenginleştirilmelidir.',
            'Aşırı sulamadan kaçınılmana özen gösterilmelidir.'
        ],
        'recipe_preview': 'Limon tuzu yardımıyla şelatlanan demir sülfat çözeltisi akşam serinliğinde yapraktan uygulanmalı, toprak pH seviyesi kükürt ile düşürülmelidir.'
    },
    {
        'slug': 'tutun-beyazsinegi-yaz',
        'title': 'Tütün Beyazsineği Zararı',
        'scientific_name': 'Bemisia tabaci',
        'category': 'Zararlı İstilası',
        'season': 'Yaz',
        'risk_level': 'Yüksek',
        'description': 'Yaz aylarında pamuk, domates ve biber seralarında yaprak altlarında kolonileşerek özsu emen ve bitkisel virüsleri taşıyan çok küçük beyaz böceklerdir.',
        'symptoms': [
            'Yapraklar sallandığında havaya uçuşan küçük beyaz sinek bulutu',
            'Yaprakların alt yüzeyinde sarımsı larva ve yumurtaların bulunması',
            'Bitkilerde gelişim geriliği ve yapraklarda yapışkan balımsı madde birikimi'
        ],
        'favorable_conditions': '30°C üzeri yüksek sıcaklıklar, rüzgarsız seralar ve sık dikim yapılmış alanlar.',
        'case_scenario': 'Ağustos ayında sera kapısından giren çiftçi, domates yapraklarına dokununca binlerce beyaz sineğin uçuştuğunu görür. Beyazsinekler emgi yaparak bitkiyi zayıflatmanın yanında mozaik virüsünü de bulaştırır, hasat yarı yarıya düşer.',
        'organic_recipe_name': 'Fesleğen ve Neem Yağı Koruyucu',
        'organic_recipe_prep': '10 litre suya 30 ml neem yağı, 10 ml kekik yağı and 24 saat bekletilmiş taze fesleğen suyu eklenerek karıştırılır.',
        'organic_recipe_app': 'Yaprak altlarını hedef alarak sisleme şeklinde uygulanır. Beyazsineklerin kokudan kaçması ve yumurta bırakamaması sağlanır.',
        'preventative_measures': [
            'Seraya girişlerde ince gözenekli böcek tülleri (custom net) kullanılmalıdır.',
            'Sera içine sarı yapışkan tuzaklar yoğun bir şekilde asılmalıdır.',
            'Avcı böcek (Macrolophus pygmaeus) popülasyonu desteklenerek biyolojik mücadele yapılmalıdır.'
        ],
        'recipe_preview': 'Sarı yapışkan tuzaklar asılmalı, yaprak altlarına neem ve kekik yağlı bitki kaçırıcı karışım haftalık olarak püskürtülmelidir.'
    },

    # SONBAHAR MEVSİMİ (6 Öğe)
    {
        'slug': 'zeytin-sinegi-sonbahar',
        'title': 'Zeytin Sineği Tahribatı',
        'scientific_name': 'Bactrocera oleae',
        'category': 'Zararlı İstilası',
        'season': 'Sonbahar',
        'risk_level': 'Çok Yüksek',
        'description': 'Eylül ve Ekim aylarında zeytin meyvelerine yumurta bırakarak larvaların içeride beslenmesini sağlayan, zeytinyağı asitliğini artıran ve döküme yol açan sinektir.',
        'symptoms': [
            'Zeytin meyvesi üzerinde sineğin yumurta bıraktığı V şeklinde küçük yaralar',
            'Meyve içinde beslenen beyaz larvaların açtığı tüneller',
            'Zeytinlerin vaktinden önce kararıp yumuşaması ve yere dökülmesi'
        ],
        'favorable_conditions': '20-25°C sıcaklıklar, nemli ve yağışlı sonbahar günleri.',
        'case_scenario': 'Eylül sonunda zeytinlikte gezen üretici, tanelerin üzerinde küçük delikler ve kararmalar fark eder. Zeytinler sıkıldığında kurtçuklar dışarı çıkar. Hasat edilen zeytinlerin yağı yüksek asitli çıkar ve sofralık değeri kalmaz.',
        'organic_recipe_name': 'Kaolin Kili ve Arap Sabunu Zırhı',
        'organic_recipe_prep': '100 litre suya 3 kg kaolin kili ve kilin yaprağa yapışması için 200 ml sıvı arap sabunu karıştırılarak bulamaç hazırlanır.',
        'organic_recipe_app': 'Zeytin meyveleri nohut büyüklüğüne ulaştığı andan itibaren tüm ağacı kaplayacak şekilde beyaz bir örtü halinde püskürtülür. Sineğin meyveyi algılaması engellenir.',
        'preventative_measures': [
            'Hasat sonrası yere dökülen kurtlu zeytinler toplanıp imha edilmelidir.',
            'Ağaçlar budanarak iç kısımlarının güneş alması ve kuru kalması sağlanmalıdır.',
            'Toprak sonbaharda sürülerek pupaların kış soğuğunda ölmesi sağlanmalıdır.'
        ],
        'recipe_preview': 'Kaolin kili uygulaması ile ağaçlar beyaza boyanarak sineğin meyveyi görmesi engellenmeli, sonbaharda toprak derin sürülmelidir.'
    },
    {
        'slug': 'bag-kullemesi-sonbahar',
        'title': 'Bağda Külleme Hastalığı',
        'scientific_name': 'Uncinula necator',
        'category': 'Fungus Yayılımı',
        'season': 'Sonbahar',
        'risk_level': 'Yüksek',
        'description': 'Bağlarda asma yapraklarında, sürgünlerde ve özellikle üzüm salkımlarında beyaz unsu tabaka oluşturan, üzümleri çatlatan fungal bir enfeksiyondur.',
        'symptoms': [
            'Yapraklarda ve salkım çöplerinde un serpilmiş gibi kirli beyaz tozlu görünüm',
            'Üzüm tanelerinin büyüyemeyerek çatlaması ve çekirdeklerinin dışarı fırlaması',
            'Sonbaharda sürgünlerin üzerinde siyah-kahverengi lekelerin (kışlık gözlerin) belirmesi'
        ],
        'favorable_conditions': '20-27°C sıcaklık, orta nemli ve gölgeli havasız bağ yapıları.',
        'case_scenario': 'Hasat dönemi yaklaşırken asmaların yapraklarında unsu tabaka belirir. Üzümler çatlayarak çürümeye başlar. Şaraplık ve sofralık üzümlerde büyük kalite kaybı yaşanır.',
        'organic_recipe_name': 'Potasyum Bikarbonat ve Süt Emülsiyonu',
        'organic_recipe_prep': '10 litre suya 40 gram potasyum bikarbonat, 1 litre yağsız süt ve 20 ml neem yağı karıştırılır.',
        'organic_recipe_app': 'Salkımlara ve yapraklara nüfuz edecek şekilde homojen püskürtülür. Budama sonrası kışlık sporları azaltmak için gövdeye de uygulanır.',
        'preventative_measures': [
            'Asmaların iç kısımları budanarak mükemmel bir hava sirkülasyonu ve güneşlenme sağlanmalıdır.',
            'Yere dökülen hastalıklı yapraklar toplanarak bağdan uzaklaştırılmalıdır.',
            'Azotlu gübre miktarı sınırlandırılmalıdır.'
        ],
        'recipe_preview': 'Hava sirkülasyonu budama ile artırılmalı, potasyum bikarbonat ve süt karışımı salkımlara koruyucu olarak püskürtülmelidir.'
    },
    {
        'slug': 'lahana-guvesi-sonbahar',
        'title': 'Lahana Yaprak Güvesi Hasarı',
        'scientific_name': 'Plutella xylostella',
        'category': 'Zararlı İstilası',
        'season': 'Sonbahar',
        'risk_level': 'Orta',
        'description': 'Lahana, brokoli ve karnabahar yapraklarının alt dokularını yiyerek dantel gibi delik deşik eden küçük yeşil larvalardır.',
        'symptoms': [
            'Yapraklarda sadece üst zarın kaldığı şeffaf pencere şeklinde pencereler',
            'Yaprakların delik deşik olması ve bitkinin göbek bağlayamaması',
            'Larvaların dokunulduğunda ipek iplikle kendini aşağı sarkıtması'
        ],
        'favorable_conditions': '18-24°C sıcaklıklar, nemli sonbahar sabahları.',
        'case_scenario': 'Ekim ayında lahana tarlasında yaprakların delik deşik olduğu görülür. Yaprakların altına bakıldığında ince yeşil kurtçukların yaprak etini yediği anlaşılır. Bitkiler gelişimini durdurur ve baş yapamaz.',
        'organic_recipe_name': 'Sarımsak ve Pul Biber Ekstratı',
        'organic_recipe_prep': '10 litre suya 5 baş ezilmiş sarımsak, 50 gram acı pul biber eklenip 24 saat bekletilir, süzüldükten sonra 30 ml sıvı sabun eklenir.',
        'organic_recipe_app': 'Lahana göbeklerine ve yaprak arkalarına püskürtülür. Acı su larvaları kaçırır ve beslenmelerini engeller.',
        'preventative_measures': [
            'Hasat sonrası lahana kökleri tarlada bırakılmamalı, derin sürümle yok edilmelidir.',
            'Lahana aralarına böcek kaçırıcı nane veya kekik ekilmelidir.',
            'Kuşlar ve parazit arıcıklar gibi doğal avcıların bahçede barınması sağlanmalıdır.'
        ],
        'recipe_preview': 'Lahana yaprakları delinmeye başladığında sarımsak ve acı biber ekstratı püskürtülmeli, hasat artıkları tarladan temizlenmelidir.'
    },
    {
        'slug': 'cilek-yaprak-lekesi-sonbahar',
        'title': 'Çilek Yaprak Lekesi Hastalığı',
        'scientific_name': 'Mycosphaerella fragariae',
        'category': 'Fungus Yayılımı',
        'season': 'Sonbahar',
        'risk_level': 'Düşük-Orta',
        'description': 'Sonbahar yağışlarıyla çilek yapraklarında ortası beyaz, kenarları mor daireler oluşturan ve bitkiyi zayıflatan fungal yaprak hastalığıdir.',
        'symptoms': [
            'Yapraklarda 3-6 mm çapında, ortası beyaz-gri, etrafı mor-kırmızı halkalı lekeler',
            'Lekelerin birleşmesiyle yaprakların kuruması',
            'Meyve saplarında lezyonlar oluşması ve meyvelerin küçülmesi'
        ],
        'favorable_conditions': '10-20°C serin hava, sık dikim, aşırı nemli ve sisli sonbahar havası.',
        'case_scenario': 'Kasım ayında çilek tarhlarında yaprakların üzeri kırmızı beneklerle dolar. Bu beneklerin ortası grileşir. Yaprak alanı azalan çilekler kışa zayıf girer ve bahardaki meyve verimi düşer.',
        'organic_recipe_name': 'Bordo Bulamacı Uygulaması',
        'organic_recipe_prep': 'Organik tarıma uygun %1\'lik bordo bulamacı (bakır sülfat ve sönmüş kireç karışımı) hazırlanır.',
        'organic_recipe_app': 'Sonbahar yağmurlarından önce ve sonra tüm çilek yapraklarını kaplayacak şekilde püskürtülür. Sporların çimlenmesi engellenir.',
        'preventative_measures': [
            'Çilek sıraları arasında biriken eski yapraklar budanarak temizlenmelidir.',
            'Malçlama yenilenerek toprak neminin yapraklara sıçraması önlenmelidir.',
            'Dayanıklı fide çeşitleri tercih edilmelidir.'
        ],
        'recipe_preview': 'Sonbahar başlangıcında eski yapraklar budanmalı ve koruyucu olarak organik tarıma uygun bordo bulamacı püskürtülmelidir.'
    },
    {
        'slug': 'patates-mildiyosu-sonbahar',
        'title': 'Patates Mildiyösü Hastalığı',
        'scientific_name': 'Phytophthora infestans',
        'category': 'Fungus Yayılımı',
        'season': 'Sonbahar',
        'risk_level': 'Yüksek',
        'description': 'Sonbahar hasadı öncesi patates yapraklarında ıslak lekeler ve yumrularda kahverengi çürümeler oluşturan, patatesi depoda çürüten mantardır.',
        'symptoms': [
            'Yaprak uçlarından başlayan haşlanmış benzeri koyu renkli lekeler',
            'Nemli sabahlarda leke kenarlarında beyaz kül benzeri küf örtüsü',
            'Patates yumrularının kabuğunda kuru, çökük kahverengi lekeler ve iç kısımda pas rengi çürüme'
        ],
        'favorable_conditions': '15-20°C serin hava, çiğ ve sis, yetersiz havalanan ağır topraklar.',
        'case_scenario': 'Eylül ayında patates tarlasında mildiyö baş gösterir. Yapraklar kurur. Hasat edilen patatesler depoya konulduktan birkaç hafta sonra depodaki tüm patateslerin sulanıp çürüdüğü ve koktuğu fark edilir.',
        'organic_recipe_name': 'Atkuyruğu Otu ve Bakır Hidroksit Solüsyonu',
        'organic_recipe_prep': '10 litre suya 24 saat kaynatılmış atkuyruğu otu ekstraktı ve 20 gram bakır hidroksit eklenerek hazırlanır.',
        'organic_recipe_app': 'Yağmurlardan önce koruyucu olarak yapraklara uygulanır. Depolamadan önce patates yumruları iyice kurutulmalıdır.',
        'preventative_measures': [
            'Sertifikalı temiz tohumluk patates kullanılmalıdır.',
            'Hastalıklı bitki artıkları sökülüp tarladan uzaklaştırılmalıdır.',
            'Hasattan 2 hafta önce patates yaprakları biçilerek mantarın yumrulara geçişi engellenmelidir.'
        ],
        'recipe_preview': 'Hasattan 2 hafta önce yeşil aksam biçilmeli, depolama öncesi yumrular kurutulmalı ve koruyucu bakır uygulamaları aksatılmamalıdır.'
    },
    {
        'slug': 'misir-pasi-sonbahar',
        'title': 'Mısır Yaprak Pası Hastalığı',
        'scientific_name': 'Puccinia sorghi',
        'category': 'Fungus Yayılımı',
        'season': 'Sonbahar',
        'risk_level': 'Orta',
        'description': 'Mısır yapraklarında turuncu-kahverengi püstüller (kabarcıklar) oluşturan, yaprakların fotosentez gücünü azaltıp koçan dolumunu zayıflatan mantardır.',
        'symptoms': [
            'Yaprağın her iki yüzeyinde küçük, oval, tarçın kahverengisi püstüller',
            'Püstüllerin patlamasıyla etrafa yayılan toz şeklinde turuncu sporlar',
            'Şiddetli durumlarda yaprakların sararıp kuruması ve koçanların küçük kalması'
        ],
        'favorable_conditions': '16-23°C sıcaklıklar, yüksek bağıl nem (%95) ve sisli sonbahar sabahları.',
        'case_scenario': 'Eylül ayında mısır tarlasında yaprakların üzeri turuncu pürüzlerle kaplanır. Rüzgar estikçe havaya turuncu tozlar yayılır. Bitkiler erken kurur, bu yüzden koçanlardaki daneler tam dolamaz ve koçanlar küçük kalır.',
        'organic_recipe_name': 'Karahindiba ve Isırgan Otu Bağışıklık Aşısı',
        'organic_recipe_prep': '10 litre suya fermente edilmiş ısırgan otu suyu ve karahindiba yaprağı çayı karıştırılarak zengin mantar önleyici sıvı elde edilir.',
        'organic_recipe_app': 'Mısır koçan bağlama döneminde yapraklara koruyucu olarak püskürtülür. Bitkinin hücre çeperini güçlendirir.',
        'preventative_measures': [
            'Dayanıklı mısır melezleri tercih edilmelidir.',
            'Münavebe yapılarak tarlaya üst üste mısır ekilmemelidir.',
            'Toprak analizine göre dengeli gübreleme yapılmalı, aşırı azottan kaçınılmalıdır.'
        ],
        'recipe_preview': 'Dengeli gübreleme yapılmalı, koçan bağlamadan itibaren ısırgan ve karahindiba ekstraktları ile yapraklar desteklenmelidir.'
    },

    # KIŞ MEVSİMİ (6 Öğe)
    {
        'slug': 'narenciye-kahverengi-curukluk-kis',
        'title': 'Narenciyede Kahverengi Çürüklük',
        'scientific_name': 'Phytophthora citrophthora',
        'category': 'Fungus Yayılımı',
        'season': 'Kış',
        'risk_level': 'Çok Yüksek',
        'description': 'Kış aylarında yağışlarla topraktan sıçrayan sporların limon, mandalina ve portakal meyvelerini kahverengileştirip çürüttüğü fungal bir hastalıktır.',
        'symptoms': [
            'Meyve kabuğunda sert, açık kahverengi ve kösele gibi lezyonlar belirmesi',
            'Meyvelerin kendine has ekşi, keskin bir koku yayarak dökülmesi',
            'Ağaç gövdesinde zamklanma (sakızlaşma) ve kabuk çatlaklarının oluşması'
        ],
        'favorable_conditions': '10-20°C sıcaklıklar, sürekli kış yağışları ve ağaç altlarının otlu olması.',
        'case_scenario': 'Aralık ayında günlerce süren yağmurlar sonrasında, limon ağaçlarının alt dallarındaki limonlar kahverengileşmeye ve dökülmeye başlar. Bahçeye girildiğinde keskin bir ekşime kokusu duyulur. Dökülen meyveler satılamaz hale gelir.',
        'organic_recipe_name': 'Göztaşı Bulamacı ve Kireç Zırhı',
        'organic_recipe_prep': '%2\'lik Bordo bulamacı hazırlanır. Ayrıca ağaç gövdelerini korumak için kireç ve göztaşı karışımı macun hazırlanır.',
        'organic_recipe_app': 'Kış yağmurları başlamadan önce ağaçların alt dalları ve toprak yüzeyi ilaçlanır. Ağaç gövdeleri yerden 1 metre yüksekliğe kadar hazırlanan macunla boyanır.',
        'preventative_measures': [
            'Ağaçların alt dalları yerden en az 50-60 cm yükseklikte olacak şekilde budanmalıdır.',
            'Ağaç diplerindeki yabancı otlar temizlenerek hava akımı sağlanmalıdır.',
            'Toprakta su birikmesi önlenmeli, drenaj kanalları açık tutulmalıdır.'
        ],
        'recipe_preview': 'Ağaç gövdeleri kireç ve göztaşıyla boyanmalı, alt dallar etek budamasıyla yerden yükseltilmeli ve kış yağmurlarından önce bordo bulamacı atılmalıdır.'
    },
    {
        'slug': 'bakteriyel-kanser-kis',
        'title': 'Domateste Bakteriyel Kanser Hastalığı',
        'scientific_name': 'Clavibacter michiganensis subsp. michiganensis',
        'category': 'Bakteri Girişi',
        'season': 'Kış',
        'risk_level': 'Yüksek',
        'description': 'Kışlık sera domateslerinde tohum veya yaralardan bulaşarak iletim demetlerini tıkayan, yaprakları kurutan ve meyvelerde kuş gözü lekeleri yapan tehlikeli bakteridir.',
        'symptoms': [
            'Yaprak kenarlarının yukarı doğru kıvrılıp kuruması ve esmerleşmesi',
            'Gövde boyuna kesildiğinde iletim demetlerinin sarı-kahverengi renge dönmesi',
            'Meyve yüzeyinde ortası kahverengi, etrafı beyaz halkalı (kuş gözü) küçük lekeler'
        ],
        'favorable_conditions': 'Sera içi yüksek nem, yetersiz havalandırma, serin kış günleri (18-24°C) ve budama yaraları.',
        'case_scenario': 'Ocak ayında kışlık domates serasında bazı bitkilerin tek taraflı yapraklarının kuruduğu fark edilir. Meyvelerin üzerinde kuş gözüne benzeyen lekeler belirir. Bakteri budama makaslarıyla tüm sıraya yayıldığı için sera karantinaya alınır.',
        'organic_recipe_name': 'Defne Yağı ve Bakır Oktaonat Kalkanı',
        'organic_recipe_prep': '10 litre suya 25 gram bakır oktaonat ve antibakteriyel etkisiyle bilinen 15 ml saf defne yağı eklenerek karıştırılır.',
        'organic_recipe_app': 'Budama sonrasında tüm yaraları kapatacak şekilde sisleme halinde püskürtülür. Aletler her bitkide alkolle sterilize edilir.',
        'preventative_measures': [
            'Kesinlikle sertifikalı, temiz ve dezenfekte edilmiş tohumlar/fideler kullanılmalıdır.',
            'Hasta bitkiler sökülerek seradan uzaklaştırılmalı ve yakılmalıdır.',
            'Budama ve koltuk alma işlemleri sadece kuru ve güneşli havalarda yapılmalıdır.'
        ],
        'recipe_preview': 'Sertifikalı tohum kullanılmalı, koltuk alma işlemleri sadece kuru havalarda yapılmalı ve aletler sürekli dezenfekte edilmelidir.'
    },
    {
        'slug': 'sera-beyazsinegi-kis',
        'title': 'Sera Beyazsineği İstilası',
        'scientific_name': 'Trialeurodes vaporariorum',
        'category': 'Zararlı İstilası',
        'season': 'Kış',
        'risk_level': 'Orta',
        'description': 'Kışın ısıtılan seralarda domates, hıyar ve patlıcan yapraklarında beslenen, bitki özsuyunu sömüren ve mantar oluşumunu tetikleyen zararlıdır.',
        'symptoms': [
            'Yapraklara dokunulduğunda uçuşan çok sayıda beyaz sinek',
            'Yaprak altlarında sarımsı-yeşil renkli hareketsiz larvalar',
            'Yaprakların yapışkan tatlımsı maddeyle kaplanması ve siyahlaşması'
        ],
        'favorable_conditions': '20-25°C sıcaklığa sahip kışlık ısıtmalı seralar, düşük hava sirkülasyonu.',
        'case_scenario': 'Şubat ayında hıyar serasında yaprakların kurumaya başladığı görülür. Bitki özsuyunu emen beyazsinek larvaları, bitkileri halsiz bırakır ve salgıladıkları tatlı sıvı yüzünden meyveler yapış yapış olarak pazar değerini yitirir.',
        'organic_recipe_name': 'Sarımsak ve Neem Yağı Emülsiyonu',
        'organic_recipe_prep': '10 litre suya 5 baş ezilmiş sarımsak suyu, 30 ml soğuk pres neem yağı ve yapışmayı artırmak için 30 ml sıvı sabun karıştırılır.',
        'organic_recipe_app': 'Yaprak altlarına odaklanarak haftada bir kez püskürtülür. Larvaların nefes alması engellenir.',
        'preventative_measures': [
            'Sera pencerelerine ince sineklik tülleri takılarak sinek girişi engellenmelidir.',
            'Sari yapışkan tuzaklar bitkilerin hemen üzerine gelecek şekilde asılmalıdır.',
            'Faydalı parazit arıcıklar (Encarsia formosa) seraya salınarak biyolojik mücadele yapılmalıdır.'
        ],
        'recipe_preview': 'Sarı yapışkan tuzaklar asılmalı, sarımsak ve neem yağı emülsiyonu ile yaprak altları düzenli olarak ilaçlanmalıdır.'
    },
    {
        'slug': 'marul-kursuni-kuf-kis',
        'title': 'Marulda Kurşuni Küf Hastalığı',
        'scientific_name': 'Botrytis cinerea',
        'category': 'Fungus Yayılımı',
        'season': 'Kış',
        'risk_level': 'Yüksek',
        'description': 'Kışlık sera marullarında yüksek nem ve soğuk havalarda göbek kısmından başlayan kurşuni renkli küf tabakasıyla bitkiyi çürüten mantardır.',
        'symptoms': [
            'Kök boğazına yakın yapraklarda sulu, kahverengi lekeler oluşması',
            'Nemli koşullarda bu lekelerin üzerinde gri-kurşuni renkte tozlu küf tabakası belirmesi',
            'Marul göbeğinin tamamen yumuşayarak çürümesi ve kokması'
        ],
        'favorable_conditions': '15-20°C serin sıcaklıklar, %95 üzeri aşırı bağıl nem, gölgede kalma ve don olayları sonrasındaki zayıflık.',
        'case_scenario': 'Ocak ayında havalandırılmayan marul serasında sabahları yoğun sis oluşur. Marulların alt yapraklarında gri küfler yayılmaya başlar. Hasat zamanı gelen marulların ortaları çürüyerek dağılır.',
        'organic_recipe_name': 'Karbonat ve Tarçın Yağı Mantar Savar',
        'organic_recipe_prep': '10 litre suya 50 gram sodyum bikarbonat (karbonat), 20 ml saf tarçın yağı ve 30 ml sıvı sabun eklenerek karıştırılır.',
        'organic_recipe_app': 'Sabah erken saatlerde, çiğ kalktıktan sonra marulların göbek kısımlarına ve alt yapraklarına püskürtülür.',
        'preventative_measures': [
            'Seranın havalandırılmasına azami özen gösterilmeli, nem %80 altına düşürülmelidir.',
            'Sık ekimden kaçınılmalı, damlama sulama ile sulama yapılmalıdır.',
            'Çürüyen bitkiler eldivenle toplanıp poşete konarak seradan uzaklaştırılmalıdır.'
        ],
        'recipe_preview': 'Nem seviyesi havalandırma ile düşürülmeli, çürük yapraklar temizlenmeli ve göbek kısımlarına karbonat-tarçın yağı solüsyonu uygulanmalıdır.'
    },
    {
        'slug': 'narenciye-unlu-bit-kis',
        'title': 'Narenciye Unlu Biti',
        'scientific_name': 'Planococcus citri',
        'category': 'Zararlı İstilası',
        'season': 'Kış',
        'risk_level': 'Orta-Yüksek',
        'description': 'Kış aylarında narenciye ağaçlarının gövde çatlaklarında, meyve saplarında beyaz unsu pamuksu kitleler halinde yaşayan ve özsu emen zararlıdır.',
        'symptoms': [
            'Meyve saplarında ve gövdede beyaz, unsu, pamuk gibi görünen böcek kitleleri',
            'Meyvelerin dökülmesi, yaprakların sararması',
            'Ağaç üzerinde yoğun karıncalanma görülmesi'
        ],
        'favorable_conditions': 'Ilıman geçen kış günleri, sık dikilmiş esintisiz bahçeler, budanmamış sık ağaçlar.',
        'case_scenario': 'Ocak ayında portakal bahçesinde portakalların sap kısımlarında beyaz unsu yığınlar fark edilir. Bitki özsuyunu emen unlu bitler portakalların saplarını zayıflatarak dökülmelerine yol açar. Meyveler lekeli ve kirli görünür.',
        'organic_recipe_name': 'Bitkisel Yağ ve Arap Sabunu Karışımı',
        'organic_recipe_prep': '10 litre suya 150 ml yazlık mineral yağ veya saf ayçiçek yağı, 100 ml sıvı arap sabunu ve 20 ml kekik yağı karıştırılır.',
        'organic_recipe_app': 'Beyaz kitlelerin üzerine gelecek şekilde yüksek basınçlı pülverizatörle püskürtülür. Yağ tabakası böceği kaplayarak havasız bırakır.',
        'preventative_measures': [
            'Ağaçların gövdeleri temiz tutulmalı, kuru kabuklar fırçalanmalıdır.',
            'Ağaç diplerindeki karınca yuvaları engellenmelidir çünkü karıncalar unlu bitleri korur.',
            'Biyolojik mücadelede avcı böcek Cryptolaemus montrouzieri salımı yapılmalıdır.'
        ],
        'recipe_preview': 'Karınca popülasyonu engellenmeli, pamuksu kitlelerin üzerine bitkisel yağ ve arap sabunu karışımı basınçlı şekilde püskürtülmelidir.'
    },
    {
        'slug': 'kok-uru-nematodu-kis',
        'title': 'Kök Uru Nematodu Hasarı',
        'scientific_name': 'Meloidogyne spp.',
        'category': 'Toprak Mantarı',
        'season': 'Kış',
        'risk_level': 'Yüksek',
        'description': 'Bitki köklerinin içine yerleşerek irili ufaklı urlar (şişlikler) oluşturan, köklerin su ve besin almasını engelleyen mikroskobik solucanlardır.',
        'symptoms': [
            'Sökülen bitki köklerinde tespih tanesi gibi dizilmiş urlar ve nodüller',
            'Bitkinin sulansa dahi gün ortasında solgun görünmesi ve büyümesinin durması',
            'Yapraklarda besin eksikliği belirtileri ve sararmaların baş göstermesi'
        ],
        'favorable_conditions': 'Killi-kumlu gevşek topraklar, nemli toprak yapısı, üst üste hassas bitki ekimi yapılması.',
        'case_scenario': 'Şubat ayında sera içi hıyarlarda yapraklar sararmaya ve solmaya başlar. Gübreleme ve sulamaya rağmen düzelme olmaz. Bitki söküldüğünde saçak kökler yerine yumru şeklinde dev urlar görülür. Nematod kökü felç etmiştir.',
        'organic_recipe_name': 'Kadife Çiçeği Ekstratı ve Kekik Yağı Toprak Aşısı',
        'organic_recipe_prep': 'Kurutulmuş kadife çiçeği yapraklarından elde edilen konsantre su ve 10 litre suya 50 ml kekik yağı karıştırılarak hazırlanır.',
        'organic_recipe_app': 'Damlama sulama sistemi ile doğrudan kök bölgesine toprak şerbeti şeklinde verilir. Kadife çiçeğindeki doğal salgılar nematodları öldürür.',
        'preventative_measures': [
            'Bahçede çilek veya sebze aralarına yoğun şekilde Kadife Çiçeği (Tagetes) dikilmelidir.',
            'Hasat sonrası toprak kışın derin sürülerek alt üst edilmeli ve donmaya bırakılmalıdır.',
            'Nematoda dayanıklı anaçlar üzerine aşılı fideler tercih edilmelidir.'
        ],
        'recipe_preview': 'Nematoda dayanıklı anaç kullanılmalı, dikim aralarına kadife çiçeği ekilmeli ve toprağa kekik yağlı şerbet aşılanmalıdır.'
    }
]

def run():
    print(f"Toplam {len(ALL_SEED_ITEMS)} adet tarla rehberi verisi veritabanına ekleniyor...")
    count = 0
    for val in ALL_SEED_ITEMS:
        # Check if item with this slug already exists to prevent duplicate key errors
        if FieldGuideItem.objects.filter(slug=val['slug']).exists():
            # Update values if it already exists
            item = FieldGuideItem.objects.get(slug=val['slug'])
            item.title = val['title']
            item.scientific_name = val['scientific_name']
            item.category = val['category']
            item.season = val['season']
            item.risk_level = val['risk_level']
            item.description = val['description']
            item.symptoms = val['symptoms']
            item.favorable_conditions = val['favorable_conditions']
            item.case_scenario = val['case_scenario']
            item.organic_recipe_name = val['organic_recipe_name']
            item.organic_recipe_prep = val['organic_recipe_prep']
            item.organic_recipe_app = val['organic_recipe_app']
            item.preventative_measures = val['preventative_measures']
            item.recipe_preview = val['recipe_preview']
            item.save()
            print(f"Güncellendi: {item.title} ({item.season})")
            count += 1
            continue
            
        item = FieldGuideItem(
            slug=val['slug'],
            title=val['title'],
            scientific_name=val['scientific_name'],
            category=val['category'],
            season=val['season'],
            risk_level=val['risk_level'],
            description=val['description'],
            symptoms=val['symptoms'],
            favorable_conditions=val['favorable_conditions'],
            case_scenario=val['case_scenario'],
            organic_recipe_name=val['organic_recipe_name'],
            organic_recipe_prep=val['organic_recipe_prep'],
            organic_recipe_app=val['organic_recipe_app'],
            preventative_measures=val['preventative_measures'],
            recipe_preview=val['recipe_preview'],
            pros=[],
            cons=[]
        )
        item.save()
        count += 1
        print(f"Eklendi: {item.title} ({item.season})")
    print(f"Tamamlandı! {count} adet tarla rehberi verisi başarıyla eklendi/güncellendi.")

if __name__ == '__main__':
    run()
