import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from field_guide.models import FieldGuideItem

# We can access REHBER_DATA inside views.py by reading views.py or getting it from a small trick.
# Since REHBER_DATA is defined inside tarla_rehberi_detay_view, let's extract it or recreate it.
# Actually, to make it robust, we can copy the REHBER_DATA dictionary from views.py directly in this script.

REHBER_DATA = {
    'cokerten-hastaligi': {
        'title': 'Çökerten Hastalığı (Damping-Off)',
        'scientific_name': 'Pythium spp., Rhizoctonia solani, Phytophthora spp.',
        'category': 'Fungus Yayılımı',
        'season': 'İlkbahar',
        'risk_level': 'Yüksek',
        'description': 'Yeni çimlenen fidelerin kök boğazı bölgesindeki taze ve nazik dokuların çürüyerek incelmesi ve fidenin devrilmesiyle sonuçlanan fungal bir hastalıktır.',
        'symptoms': [
            'Kök boğazında ıslak görünümlü, esmerleşen lezyonlar',
            'Fidenin gövdesinin zeminle birleştiği noktada ipliksi incelme',
            'Fidelerin ayakta duramayarak aniden topluca devrilmesi'
        ],
        'favorable_conditions': '10-15°C civarındaki düşük toprak sıcaklıkları, %85 üzeri aşırı bağıl nem, gölge fide yatakları ve aşırı azotlu gübreleme.',
        'case_scenario': 'Özellikle Mart sonu Nisan başı gibi ısıtmasız plastik tünellerde veya fide yataklarında, havanın günlerce bulutlu gittiği nemli ilkbahar sabahlarında, can suyunun fazla verilmesi sebebiyle toprak kuruyamaz. 48 saat içinde fungal sporlar aktifleşerek domates ve biber fidelerini kök boğazından eritir; sabah seraya giren çiftçi fidelerin neredeyse tamamının devrildiğini görür.',
        'organic_recipe_name': 'Trichoderma ve Odun Külü Kalkanı',
        'organic_recipe_prep': '10 filtre dinlendirilmiş klorsuz suya 50 gram Trichoderma harzianum (faydalı mantar sporları) eklenir ve 2 saat aktifleştirilir. Toprak yüzeyine ince bir tabaka odun külü tozlanır.',
        'organic_recipe_app': 'Tohum ekimi sırasında ve fideler şaşırtıldıktan hemen sonra can suyu olarak kök bölgesine uygulanır. 15 gün sonra uygulama tekrarlanmalıdır.',
        'preventative_measures': [
            'Her ekim döneminden önce fide viyolleri ve toprak sterilize edilmelidir.',
            'Fideler arasında hava sirkülasyonunu sağlamak için sık dikimden kaçınılmalıdır.',
            'Sulama periyotları mutlaka sabah erken saatlerde planlanarak toprağın geceye ıslak girmesi önlenmelidir.'
        ]
    },
    'yaprak-bitleri': {
        'title': 'Yaprak Bitleri ve Thrips Saldırısı',
        'scientific_name': 'Aphis gossypii, Thrips tabaci',
        'category': 'Zararlı İstilası',
        'season': 'İlkbahar',
        'risk_level': 'Orta-Yüksek',
        'description': 'Taze vevejetatif büyüme dönemindeki bitki özsuyunu emerek yaprakların kıvrılmasına, sararmasına ve domates lekeli solgunluk virüsü (TSWV) gibi ölümcül virüslerin yayılmasına sebep olan emici böcek saldırısıdır.',
        'symptoms': [
            'Taze yapraklarda aşağıya doğru büzülme ve kıvrılma',
            'Zararlıların arkasında bıraktığı yapışkan, tatlımsı madde (fümajine yol açar)',
            'Yaprakların alt yüzeylerinde küçük yeşil, siyah veya sarı böcek kolonileri'
        ],
        'favorable_conditions': 'Havaların 18-24°C sıcaklığa ulaştığı, taze sürgünlerin bol olduğu kurak ilkbahar günleri.',
        'case_scenario': 'Nisan ayında havaların aniden ısınmasıyla biber ve patlıcan yapraklarında hızlı sürgün gelişimi başlar. Bu dönemde rüzgarla gelen kanatlı yaprak bitleri, taze tepe sürgünlerine yerleşerek hızla ürer. Bitki özsuyunu emerek yaprakleri kubbeleştirir. İlerleyen günlerde virüs taşıyan thripslerin de gelmesiyle tarlada mozaik virüsü salgını başlar ve verim %80 oranında düşer.',
        'organic_recipe_name': 'Arap Sabunlu Sarımsak ve Neem Maseratı',
        'organic_recipe_prep': '3 baş sarımsak ezilerek 1 litre suda 24 saat bekletilir. Süzüldükten sonra üzerine 10 litre su, 50 ml organik neem yağı (soğuk pres) ve 2 yemek kaşığı sıvı arap sabunu eklenerek iyice çalkalanır.',
        'organic_recipe_app': 'Rüzgarsız günlerde, doğrudan güneş ışığının olmadığı akşamüstü saatlerinde, yaprakların özellikle alt yüzeylerine kaplama şeklinde püskürtülür.',
        'preventative_measures': [
            'Fide dikimiyle birlikte sıra üzerlerine sarı ve mavi yapışkan tuzaklar asılmalıdır.',
            'Tarla çevresindeki yabancı otlar zararlılara konukçuluk ettiği için temizlenmelidir.',
            'Uğur böcekleri ve avcı böcekleri tarlaya çekmek için kimyasal herbisit kullanımı sınırlandırılmalıdır.'
        ]
    },
    'demir-klorozu': {
        'title': 'Demir Klorozu ve Yaprak Sararması',
        'scientific_name': 'Fizyolojik Demir (Fe) Noksanlığı',
        'category': 'Toprak Fizyolojisi',
        'season': 'İlkbahar',
        'risk_level': 'Orta',
        'description': 'Yüksek kireçli ve alkali topraklarda bitkinin demir iyonlarını alamaması sonucu en genç yapraklarda damarlar yeşil kalırken araların sararmasıyla kendini gösteren fizyolojik bozukluktur.',
        'symptoms': [
            'En genç (tepe) yapraklarda başlayan sararma',
            'Yaprak damarlarının koyu yeşil, damar aralarının ise saman sarısı kalması',
            'Şiddetli vakalarda yaprak kenarlarında kuruma ve sürgün uçlarında ölüm'
        ],
        'favorable_conditions': 'pH derecesi 7.5\'in üzerinde olan kireçli topraklar, aşırı killi ve soğuk bahar toprakları.',
        'case_scenario': 'İlkbaharda havalar ısındığında bitkiler hızla büyümek ister ve demir ihtiyacı tavan yapar. Ancak killi ve kireçli topraklarda toprak soğuk ve ıslak olduğu için demir çözünemez. Domates veya meyve fidanlarının tepe sürgünleri 3 gün içinde tamamen sararır. Fotosentez durduğu için bitki boy atamaz, çiçek dökümleri başlar.',
        'organic_recipe_name': 'Kükürtlü Organik Demir Şelatı',
        'organic_recipe_prep': 'Toprağa pH düşürücü elementel toz kükürt karıştırılır. Yapraktan uygulama için 10 litre suya 15 gram Fe-EDDHA (organik demir şelatı) ve 10 ml organik yayıcı yapıştırıcı eklenerek karıştırılır.',
        'organic_recipe_app': 'Yapraktan hazırlanan solüsyon, sabah serinliğinde veya akşamüstü saatlerinde tepe sürgünlerine püskürtülür. Toprak uygulaması ise ilkbahar başında kök izdüşümüne yapılmalıdır.',
        'preventative_measures': [
            'Ekim öncesinde mutlaka toprak analizi yaptırarak pH seviyesi ölçülmelidir.',
            'Toprağa bol miktarda fermente edilmiş ahır gübresi veya leonardit karıştırılarak organik madde artırılmalıdır.',
            'Aşırı kireç içeren sulama suları filtrelenmeli veya asitle nötralize edilmelidir.'
        ]
    },
    'mildiyo-salgini': {
        'title': 'Mildiyö Salgını ve Güneş Yanığı',
        'scientific_name': 'Plasmopara viticola, Phytophthora infestans',
        'category': 'Isı Stresi',
        'season': 'Yaz',
        'risk_level': 'Çok Yüksek',
        'description': 'Öğleden sonra bastıran ani yaz yağmurları sonrasında yükselen aşırı nemle uyanan, yaprak altında unsu tabakalar oluşturan fungal salgın ve meyvelerde güneşin kavurmasıyla oluşan doku ölümleridir.',
        'symptoms': [
            'Yaprakların üst yüzeyinde sarımsı, alt yüzeyinde ise grimsi küf tabakası',
            'Domates ve meyve yüzeylerinde geniş, kuru, beyaz veya gümüş renkli yanık alanları',
            'Meyvelerin olgunlaşmadan yumuşayarak çürümesi ve dökülmesi'
        ],
        'favorable_conditions': '25-30°C gündüz sıcaklığı, %80 üzeri nem, ani yaz sağanakları ve dik güneş açıları.',
        'case_scenario': 'Temmuz ayında tarlada domatesler tam kızarma dönemindeyken öğleden sonra ani bir yaz sağanağı bastırır. Ardından bulutlar dağılır ve yakıcı yaz güneşi açar. Nem hızla buharlaşırken yaprakların ıslak kalması sebebiyle 24 saat içinde mildiyö mantarı uyanır. Aynı esnada yaprakları dökülen domatesler kızgın güneş ışığına doğrudan maruz kalarak haşlanır; meyvelerin alt kısımları beyaz derimsi bir hal alıp çürür.',
        'organic_recipe_name': 'Kaolin Kili ve Bakırlı Organik Çözelti',
        'organic_recipe_prep': '100 litre suya 3 kg ultra ince aktif kaolin kili eklenerek mikserle karıştırılır. Fungal koruma için karışıma 200 gram organik sertifikalı bakır sülfat eklenir.',
        'organic_recipe_app': 'Yağmur bastırmadan önce koruyucu olarak veya yağışların hemen ardından tüm yaprak ve meyve yüzeyini kaplayacak şekilde (beyaz bir film tabakası oluşturarak) püskürtülür.',
        'preventative_measures': [
            'Sıralar rüzgar yönüne paralel dikilmeli, alt yapraklar budanarak hava akımı sağlanmalıdır.',
            'Yaprakları ıslatan üstten yağmurlama sulama yerine kesinlikle damlama sulama kullanılmalıdır.',
            'Aşırı azotlu gübrelemeden kaçınarak bitkinin gevşek dokulu olması engellenmelidir.'
        ]
    },
    'fusarium-solgunlugu': {
        'title': 'Fusarium Kök Solgunluğu',
        'scientific_name': 'Fusarium oxysporum f. sp. lycopersici',
        'category': 'Toprak Mantarı',
        'season': 'Yaz',
        'risk_level': 'Yüksek',
        'description': 'Kızgın yaz güneşinde toprağın ısınmasıyla aktifleşen mantar sporlarının köklerden girerek iletim demetlerini tıkaması ve bitkiyi sulansa dahi susuz bırakıp kurutmasıdır.',
        'symptoms': [
            'Gündüz sıcak saatlerde bitkide tek taraflı solma, gece geçici olarak düzelme',
            'Alt yapraklardan başlayarak damar aralarının sararması ve kuruması',
            'Gövde kesildiğinde iletim demetlerinin (vasküler halka) kahverengiye dönmüş olması'
        ],
        'favorable_conditions': '28-32°C yüksek toprak sıcaklığı, asidik toprak pH\'ı ve taban suyu yüksek araziler.',
        'case_scenario': 'Ağustos ayında toprak sıcaklığı 30°C\'yi bulduğunda, kavun ve domates ekili tarlada bazı bitkiler öğle sıcağında solar. Çiftçi bitkinin susadığını düşünerek bol su verir. Ancak Fusarium mantarı aşırı sulanan sıcak toprakta hızla ilerleyerek kök borularını tamamen bloke eder. 3 gün içinde bitkiler gece de solgun kalmaya başlar ve nihayetinde yeşilken kuruyup ölürler.',
        'organic_recipe_name': 'Solarizasyon ve Trichoderma Aşısı',
        'organic_recipe_prep': '10 litre suya 100 ml sıvı Trichoderma harzianum eklenir ve 1 kg aktif hümik asit ile karıştırılır. Toprak solarizasyonu için yaz ortasında toprak nemlendirilip şeffaf polietilen örtüyle kaplanır.',
        'organic_recipe_app': 'Solarizasyon uygulaması yaz ortasında en az 4-6 hafta güneş altında yapılmalıdır. Ekili dönemde ise hazırlanan sıvı aşı doğrudan damlama sulama yoluyla köklere gönderilir.',
        'preventative_measures': [
            'Hastalıklı bitkiler kesinlikle tarlada bırakılmamalı, kökleriyle sökülüp yakılmalıdır.',
            'Münavebe (ekim nöbeti) uygulanarak aynı tarlaya 3 yıl üst üste solanaceae ekilmemelidir.',
            'Dayanıklı ve aşılı (örneğin yabani anaç üzerine aşılı) fideler tercih edilmelidir.'
        ]
    },
    'cicek-burnu-curuklugu': {
        'title': 'Çiçek Burnu Çürüklüğü (Blossom End Rot)',
        'scientific_name': 'Kalsiyum (Ca) Eksikliği Bozukluğu',
        'category': 'Fizyolojik Denge',
        'season': 'Yaz',
        'risk_level': 'Orta-Yüksek',
        'description': 'Sıcak yaz aylarındaki düzensiz sulamalar veya toprakta aşırı azot birikimi nedeniyle kalsiyum alımının durarak meyve uçlarında çökük, köselemsi siyah yaralar oluşturmasıdır.',
        'symptoms': [
            'Meyvenin çiçek burnu (alt kısmı) bölgesinde sulu yeşil leke belirmesi',
            'Lekenin zamanla genişleyerek kahverengi, çökük ve kuru bir hal alması',
            'Meyve içinin mantarımsı, sert ve yenilemez bir dokuya dönüşmesi'
        ],
        'favorable_conditions': 'Ekstrem yaz sıcakları, düzensiz sulama periyotları (bir kuru bir çamur toprak), yüksek tuzluluk.',
        'case_scenario': 'Yaz aylarında sulama zamanını aksatan ve toprağı tamamen kuruttuktan sonra aşırı sulayan bir üreticinin domateslerinde meyveler büyümeye başlar. Kalsiyum bitkide su akışıyla taşınabildiği için, kuraklık periyodunda meyve uçlarına kalsiyum ulaşamaz. Sonuç olarak hücre duvarları çöker ve meyve altları simsiyah derimsi bir yara alır. Hasatın %50\'si fireye gider.',
        'organic_recipe_name': 'Kalsiyum Şelatı ve Malç Koruyucu',
        'organic_recipe_prep': '10 litre suya 25 gram organik sertifikalı aminoasit şelatlı kalsiyum eklenir. Nem dengesi için toprak yüzeyi 10 cm kalınlığında saman malçı ile örtülür.',
        'organic_recipe_app': 'Kalsiyum solüsyonu, çiçeklenme döneminden itibaren yapraktan meyve salkımlarına doğrudan püskürtülür. Saman malçı ise yaz başında toprağa serilmelidir.',
        'preventative_measures': [
            'Toprak nem sensörleri yardımıyla nem seviyesi %60-70 arasında sabit tutulmalıdır.',
            'Kalsiyum emilimini bloke eden aşırı amonyum azotu (NH4) gübrelemesinden kaçınılmalıdır.',
            'Toprağın tuzluluk oranı izlenmeli, damlama sulama süreleri kısa ama sık tutulmalıdır.'
        ]
    },
    'kursuni-kuf': {
        'title': 'Kurşuni Küf Hastalığı (Grey Mold)',
        'scientific_name': 'Botrytis cinerea',
        'category': 'Nem & Küf',
        'season': 'Sonbahar',
        'risk_level': 'Yüksek',
        'description': 'Sonbahar yağmurlarıyla soğuyan serin gecelerde yaprak ve meyve saplarında biriken nem nedeniyle gri, kadifemsi mantar tabakaları oluşturan ve ürünü hızla çürüten fungal salgındır.',
        'symptoms': [
            'Meyve kabuğunda veya gövdede sulu esmerleşen lekeler',
            'Lekelerin üzerinde gri renkte kadifemsi, tozlu mantar spor tabakası',
            'Çiçek saplarının çürüyerek çiçek ve meyvelerin erken dökülmesi'
        ],
        'favorable_conditions': '15-20°C serin sonbahar sıcaklığı, %90 üzeri aşırı bağıl nem, gölgeli alanlar ve çiğ noktası oluşumu.',
        'case_scenario': 'Ekim ayında serada hasat devam ederken dışarıda soğuk sonbahar yağmurları başlar. Gece sera içi sıcaklık düşer ve havalandırma kapatılır. Tavanlarda biriken yoğuşma suları yaprakların üstüne damlar. 24 saat içinde çiçek saplarından giren Botrytis mantarı, tüm domates salkımlarını gri bir toz bulutu gibi sarar. Dokunulduğunda havaya spor yayan bu hastalık hasatı tamamen durdurur.',
        'organic_recipe_name': 'Potasyum Bikarbonat ve Havalandırma Bariyeri',
        'organic_recipe_prep': '10 litre suya 40 gram potasyum bikarbonat (alkali antifungal) ve 20 ml organik yayıcı yapıştırıcı (veya zeytinyağı bazı) eklenerek karıştırılır.',
        'organic_recipe_app': 'Seralarda havalandırma pencereleri açılarak çiğ noktası engellenir. Hazırlanan solüsyon, çiğ oluşmadan önce koruyucu olarak veya ilk lekeler görüldüğünde püskürtülür.',
        'preventative_measures': [
            'Budama yaraları, hasat edilen salkım sapları temiz tutulmalı, tarlada atık bırakılmamalıdır.',
            'Serada gece nemini düşürmek için mutlaka sirkülasyon fanları ve ısıtıcılar çalıştırılmalıdır.',
            'Bitkilerin taç yapısı budanarak iç kısımların ışık alması ve kuruması hızlandırılmalıdır.'
        ]
    },
    'bakteriyel-kanser': {
        'title': 'Bakteriyel Kanser ve Leke',
        'scientific_name': 'Clavibacter michiganensis subsp. michiganensis',
        'category': 'Bakteri Girişi',
        'season': 'Sonbahar',
        'risk_level': 'Çok Yüksek',
        'description': 'Yağmurlu ve rüzgarlı sonbahar günlerinde budama yaralarından sızan bakterilerin iletim demetlerine yerleşerek yapraklarda lekeler ve gövdede derin kanser yaraları açmasıdır.',
        'symptoms': [
            'Yaprak kenarlarında kavrulma ve aşağıya doğru kıvrılma',
            'Meyvelerde küçük, ortası koyu kahverengi, kenarı beyaz halkalı "kuş gözü" lekeleri',
            'Gövde boyuna yarıldığında sarı-kahverengi renk değişimi ve öz boşalması'
        ],
        'favorable_conditions': 'Yağışlı rüzgarlı sonbahar günleri, budama sonrası dezenfekte edilmeyen aletler, yüksek nem.',
        'case_scenario': 'Eylül sonunda serada koltuk alma budaması yapan bir işçi, budama makasını hiç sterilize etmeden yüzlerce bitkiyi budar. Rüzgar ve yağmurla birlikte yaralardan sızan bakteriler iletim borularına girer. 2 hafta içinde seradaki domates bitkilerinin yaprakları kenarlardan yanmaya başlar, gövdelerde derin kanser yaraları açılır ve bitkiler aniden çöker.',
        'organic_recipe_name': 'Doğal Bordo Bulamacı ve Alkol Kalkanı',
        'organic_recipe_prep': 'Toprak analizine göre hazırlanan %1\'lik bordo bulamacı (kalsiyum hidroksit ve bakır sülfat karışımı) taze olarak hazırlanır. Budama makasları için %70\'lik alkol solüsyonu kaplarda hazır tutulur.',
        'organic_recipe_app': 'Budama makasları her bitki değişiminde alkole batırılır. Budama işleminin tamamlanmasının hemen ardından koruyucu bordo bulamacı bitkilere püskürtülür.',
        'preventative_measures': [
            'Hastalıklı bitkiler kesinlikle tarlada bırakılmamalı, kökleriyle sökülüp yakılmalıdır.',
            'Yağmurlu ve aşırı nemli günlerde yaralar geç kapanacağı için asla budama yapılmamalıdır.',
            'Sertifikalı hastalıksız tohumlar ve sağlıklı fideler kullanılmalıdır.'
        ]
    },
    'yaprak-kulleme': {
        'title': 'Yaprak Külleme Hastalığı',
        'scientific_name': 'Oidium neolycopersici, Erysiphe spp.',
        'category': 'Fungus Yayılımı',
        'season': 'Sonbahar',
        'risk_level': 'Orta',
        'description': 'Sonbaharın kuru ve ılık geçen günlerindeki sıcaklık farklarıyla uyanan, yaprak üst yüzeyinde pudra serpilmiş gibi beyaz lekeler oluşturan ve yaprağın fotosentez yapmasını engelleyen mantardır.',
        'symptoms': [
            'Yapraklerin üst yüzeyinde dairesel, beyaz, kül benzeri lekeler',
            'Lekelerin birleşerek tüm yaprağı kaplaması ve yaprağın sararması',
            'Yaprakların kuruyarak vaktinden önce dökülmesi ve meyvelerin güneşe açık kalması'
        ],
        'favorable_conditions': '20-24°C kuru gündüzler, nemli serin geceler ve gölgeli, havasız dikim alanları.',
        'case_scenario': 'Eylül ayında gündüzler ılık, geceler ise serin ve çiğli geçer. Havasız seralarda domates yapraklarının üstünde küçük beyaz toz lekeleri belirer. Birkaç gün içinde külleme mantarı tüm yaprak yüzeylerini örter. Yapraklar fotosentez yapamadığı için meyve büyümesi durur, bitki zayıflar ve hasat sezonu erken kapanır.',
        'organic_recipe_name': 'Kükürt ve Süt Antifungal Çözeltisi',
        'organic_recipe_prep': '10 filtre suya 1 litre yağlı çiğ süt ve 9 litre klorsuz su eklenir. Fungal direnci artırmak için içerisine 30 gram ıslanabilir kükürt (Wettable Sulphur) eklenir.',
        'organic_recipe_app': 'Güneşin dik gelmediği sabah veya akşam saatlerinde, yapraklerin hem üst hem alt yüzeylerine kaplama şeklinde püskürtülür.',
        'preventative_measures': [
            'Serada havalandırma fanları çalıştırılarak bağıl nem dengelenmelidir.',
            'Bitkilerin alt yaprakları budanarak taç içi havalandırma maksimuma çıkarılmalıdır.',
            'Organik maddece zengin, dengeli gübreleme ile bitki dokularının güçlü kalması sağlanmalıdır.'
        ]
    },
    'radyasyon-donu': {
        'title': 'Radyasyon Donu ve Hücresel Ölüm',
        'scientific_name': 'Ekstrem Düşük Sıcaklık Zararı',
        'category': 'Klimatik Risk',
        'season': 'Kış',
        'risk_level': 'Çok Yüksek',
        'description': 'Rüzgarsız ve bulutsuz kış gecelerinde toprağın ısısını hızla uzaya yaymasıyla sıcaklığın aniden sıfırın altına düşmesi ve bitki hücre içi sıvısının donarak hücre çeperlerini patlatmasıdır.',
        'symptoms': [
            'Gündüz hava ısındığında yaprakların haşlanmış gibi yumuşaması ve kararması',
            'Genç sürgün uçlarında kuruma, esmerleşme ve doku ölümü',
            'Gövde kabuğunda çatlamalar ve bitkinin tamamen canlıliğini yitirmesi'
        ],
        'favorable_conditions': 'Bulutsuz, rüzgarsız kış geceleri, 0°C and altındaki ani sıcaklık düşüşleri.',
        'case_scenario': 'Ocak ayında gökyüzü tamamen berrak ve rüzgarsız bir kış gecesi başlar. Toprak gündüz depoladığı tüm ısıyı uzaya yayar (radyasyon donu) ve sıcaklık -3°C\'ye düşer. Korunmasız narenciye fidanlarının veya kışlık sebzelerin hücre içi suları donarak kristalleşir ve keskin kristalleriyle hücre çeperlerini yırtar. Sabah güneş açıp buz eridiğinde tüm yapraklar simsiyah kararır; bahçe tamamen kurur.',
        'organic_recipe_name': 'Elyaf Battaniye ve Isı Tutucu Sulama',
        'organic_recipe_prep': 'Don olayından önceki gece toprak hafifçe sulanarak suyun yüksek ısı tutma kapasitesinden faydalanılır. Genç ağaç gövdeleri samanla sarılır.',
        'organic_recipe_app': 'Bitki sıralarının üzerine UV katkılı, gözenekli beyaz agrotekstil don örtüleri çekilir. Bu örtü iç ortamı dışarıya kıyasla 3-4°C daha sıcak tutar.',
        'preventative_measures': [
            'Don riski olan günlerde açık tarlada rüzgar pervaneleri çalıştırılarak sıcak hava katmanı aşağı indirilmelidir.',
            'Fidan gövdeleri kireç bulamacı ile boyanarak kış güneşi kaynaklı ısı dalgalanmaları engellenmelidir.',
            'Aşırı azotlu kış gübrelemesinden kaçınılmalı, bitkinin sürgün vermesi uyarılmamalıdır.'
        ]
    },
    'kok-bogulmasi': {
        'title': 'Aşırı Yağış ve Kök Boğulması',
        'scientific_name': 'Toprak Anoksisi (Havasızlık) Hasarı',
        'category': 'Drenaj Hatası',
        'season': 'Kış',
        'risk_level': 'Yüksek',
        'description': 'Kış boyunca devam eden aşırı kar ve yağmur sonrasında killi arazilerde suyun göllenmesi ve kök bölgesinin günlerce oksijensiz kalarak havasız solunum (çürüme) yapmasıdır.',
        'symptoms': [
            'Yaprakların uçlardan başlayarak genel bir sararmaya maruz kalması ve dökülmesi',
            'Kök uçlarının esmerleşmesi, kokması ve çürümesi',
            'Bitkinin topraktan besin ve su alamayarak aniden kuruması'
        ],
        'favorable_conditions': 'Ağır killi toprak yapısı, kış boyu süren yoğun yağışlar ve drenaj kanalı olmayan tarlalar.',
        'case_scenario': 'Kış aylarında killi toprağa sahip bir bahçede drenaj kanalları açılmamıştır. Yağan karlar eridiğinde su tarlada göllenir ve toprak 15 gün boyunca çamur olarak kalır. Oksijensiz kalan kökler boğulur ve anaerobik bakteriler kökleri çürütür. Baharda havalar ısındığında bitkiler uyanamaz, yapraklar sararıp dökülür ve ağaçlar tamamen kurur.',
        'organic_recipe_name': 'Kompost Tahliyesi ve Kök Havalandırması',
        'organic_recipe_prep': 'Tarlanın en düşük kotlu sınırına derin tahliye kanalları açılır. Toprak yapısını gevşetmek için nehir kumu, leonardit ve yüksek kaliteli fermente kompost karıştırılır.',
        'organic_recipe_app': 'Tahliye kanalları kış girmeden önce açılmalı ve açık tutulmalıdır. Killi toprağı gevşetmek için organik kompost uygulaması sonbahar sürümünde yapılmalıdır.',
        'preventative_measures': [
            'Ağır killi arazilerde ekimler mutlaka yükseltilmiş yataklarda (sırtlarda) yapılmalıdır.',
            'Taban suyu yüksek yerlerde drenaj boruları döşenerek fazla su araziden uzaklaştırılmalıdır.',
            'Toprak işlemesi zamanında yapılmalı, ıslak toprak asla sürülmemelidir.'
        ]
    },
    'govde-catlaklari': {
        'title': 'Gövde Çatlakları ve Kış Kanseri',
        'scientific_name': 'Frost Cracking & Bark Canker',
        'category': 'Gövde Hasarı',
        'season': 'Kış',
        'risk_level': 'Orta-Yüksek',
        'description': 'Kış güneşinin gündüz fidan gövdelerini ısıtıp genleştirmesi ve gece ani donla büzüştürmesi sonucu kabukta boyuna derin yarıkların açılması ve buralardan patojenlerin sızmasıdır.',
        'symptoms': [
            'Ağaç gövdelerinde kuzey-güney yönünde boyuna uzanan derin yarıklar',
            'Yarık kenarlarında kabuk soyulmaları ve odun dokusunun açığa çıkması',
            'Yarıkların çevresinde zamk akıntısı ve kanser püstüllerinin oluşumu'
        ],
        'favorable_conditions': 'Gündüz güneşli, gece aşırı donlu (-10°C altı) kış günleri ve güneye bakan yamaçlar.',
        'case_scenario': 'Şubat ayında gündüz pırıl pırıl bir kış güneşi genç elma fidanlarının gövdesini ısıtır. Gece ise sıcaklık aniden -12°C\'ye düşer. Kabuk dokusu ani büzüşmeye dayanamayarak boyuna doğru 20 cm çatlakla yarılır. Kış boyunca bu çatlaklardan sızan kanser bakterileri ilkbaharda uyanir; fidanların gövdesinde derin kanser yaraları açarak fidanları kurutur.',
        'organic_recipe_name': 'Gövde Koruma Kireci ve Macun Kalkanı',
        'organic_recipe_prep': '10 litre suya 2 kg sönmüş kireç, 100 gram organik bakır sülfat ve 100 ml bitkisel yağ eklenerek koyu bir bulamaç hazırlanır.',
        'organic_recipe_app': 'Hazırlanan bulamaç, kış girmeden önce fırça ile ağaç gövdelerine birinci dallara kadar sürülür. Oluşan çatlaklar ise organik aşı macunu ile kapatılmalıdır.',
        'preventative_measures': [
            'Genç fidan gövdeleri kış başında saman veya hasır çuvallarla sarılarak yalıtılmalıdır.',
            'Ağaçlar rüzgardan korunmalı, gövdeyi doğrudan rüzgara maruz bırakan yönlerde rüzgar kıranlar kurulmalıdır.',
            'Budamalar kış ortasında değil, don tehlikesinin geçmeye başladığı kış sonunda yapılmalıdır.'
        ]
    },
    'acik-arazi': {
        'title': 'Açık Arazi Üretim Modeli',
        'scientific_name': 'Geleneksel Geniş Alan Tarımı',
        'category': 'Üretim Sistemi',
        'season': 'Genel',
        'risk_level': 'Yüksek',
        'description': 'Doğal iklim döngülerinin gözetildiği, başlangıç kurulum maliyeti minimum olan, geniş ölçekli geleneksel tarım ekosistemidir.',
        'symptoms': [
            'Geniş düzlüklerde büyük ölçekli mekanizasyon kullanımı',
            'Hava durumuna bağlı olarak değişen yıllık verim dalgalanmaların',
            'Doğal toprak florası ve zengin mikrobiyom varlığı'
        ],
        'favorable_conditions': 'Geniş tarım arazileri, dengeli yağış rejimleri ve mekanizasyona uygun düz coğrafyalar.',
        'case_scenario': 'Geniş bir ovada buğday, ayçiçeği veya sanayi tipi domates yetiştiren bir çiftçi, milyarlarca lira sera kurulum maliyetinden kaçınarak açık arazide üretim yapar. Doğal güneş ışığındaki tam spektrumlu UV dalga boyları sayesinde domateslerin aroması ve Briks (şeker) derecesi mükemmel olur. Ancak hasata 2 hafta kala aniden bastıran şiddetli bir dolu yağışı tüm ürünü tarlada ezer ve çiftçi sezonu sıfır ciro ile kapatır.',
        'organic_recipe_name': 'Mikrobiyal Toprak Canlandırma',
        'organic_recipe_prep': 'Dönüm başına 10 ton fermente ahır gübresi veya kompost ile birlikte mikoriza mantarları ve sıvı hümik asit karışımı hazırlanır.',
        'organic_recipe_app': 'Sonbahar sürümünde toprak derin işlenirken bu karışım toprağa karıştırılarak doğal toprak biyom bağışıklığı uyarılır.',
        'preventative_measures': [
            'Dolu riski olan bölgelerde sıra üzerlerine koruyucu dolu tülleri çekilmelidir.',
            'Toprak erozyonunu önlemek ve rüzgarı kesmek için tarla sınırlarına rüzgar kıran ağaçlar dikilmelidir.',
            'Hava durumunu yakından izleyen dijital erken uyarı sensörleri ve tarım sigortaları kullanılmalıdır.'
        ]
    },
    'sera-uretimi': {
        'title': 'Örtü Altı (Sera) Üretim Sistemi',
        'scientific_name': 'Kontrollü Alan Tarımı (Greenhouse)',
        'category': 'Üretim Sistemi',
        'season': 'Genel',
        'risk_level': 'Orta',
        'description': 'İç mekan mikro-klimasının (sıcaklık, nem, havalandırma) kontrol altında tutulduğu, yüksek birim alan verimliliği sağlayan modern korunaklı üretim modelidir.',
        'symptoms': [
            'Polikarbon, cam veya polietilen örtülü kapalı konstrüksiyonlar',
            'Askılama sistemleri ile dikey olarak büyütülen bitki yapıları',
            'Otomatik pencereler, gölgeleme perdeleri ve fan-ped soğutma üniteleri'
        ],
        'favorable_conditions': 'Yüksek verim hedeflenen pazarlara yakın alanlar, kışın çok sert geçmediği kıyı şeritleri.',
        'case_scenario': 'Kış aylarında domates fiyatlarının tavan yaptığı dönemde üretim yapmak isteyen bir girişimci, modern bir sera kurar. Sera içi mikro-klima kontrolü sayesinde kış ortasında dahi açık arazinin 5 katı verimle hasat yapar. Fiziksel bariyerler böcek geçişini engellediği için kimyasal ilaçlamaya gerek kalmaz. Ancak serada elektrik kesintisi yaşanıp havalandırma kapakları açılmadığında sera içi nem %95\'i bulur; 2 gün içinde mildiyö mantarı tüm serayı sararak üretimi felç eder.',
        'organic_recipe_name': 'Nem Kontrolü ve Entegre Mücadele',
        'organic_recipe_prep': 'Seranın çiğ noktasını engellemek için sirkülasyon fanları devreye sokulur. Fungal koruma için kükürt buharlaştırıcılar hazır bulundurulur.',
        'organic_recipe_app': 'Kükürt buharlaştırıcılar serada gece boyunca haftada 2 kez çalıştırılarak yapraklarda fungal spor oluşumu engellenir.',
        'preventative_measures': [
            'Serada çiğ noktasını ve nem yığılmasını önlemek için dijital nem sensörleri kullanılmalıdır.',
            'Tozlaşmayı sağlamak için kimyasal hormonlar yerine mutlaka Bambus arı kovanları yerleştirilmelidir.',
            'Sera girişlerine dezenfektanlı paspaslar konularak dışarıdan patojen taşınması önlenmelidir.'
        ]
    },
    'topraksiz-tarim': {
        'title': 'Topraksız & Dikey Tarım Sistemi',
        'scientific_name': 'Hidroponik & Aeroponik Ziraat',
        'category': 'Üretim Sistemi',
        'season': 'Genel',
        'risk_level': 'Düşük-Orta',
        'description': 'Toprak kullanmadan, bitki köklerinin doğrudan steril besin eriyikli su ile beslendiği, dikey katlarla birim alandan 10 kat fazla hasat sağlayan ultra-modern tarım ekosistemidir.',
        'symptoms': [
            'Köklerin kokopit, perlit veya doğrudan besinli suda (NFT) bulunması',
            'Yapay gün ışığı sunan özel spektrumlu LED grow light aydınlatmalar',
            'EC ve pH değerlerini otomatik ayarlayan dozajlama bilgisayarları'
        ],
        'favorable_conditions': 'Su kaynaklarının kısıtlı olduğu kurak bölgeler, metropol merkezleri ve steril ilaçsız ürün talebi.',
        'case_scenario': 'Metropolün ortasındaki eski bir deponun dikey topraksız tarım tesisi kuran bir teknisyen, marul ve fesleğen üretir. Kapalı devre su sirkülasyonu sayesinde su tüketimini %95 oranında azaltarak çevre dostu üretim yapar. Toprak patojenleri olmadığı için ilaç sıfırdır. Ancak rüzgarlı bir günde yaşanan büyük elektrik kesintisinde jeneratör devreye girmez. Pompalar durduğu için 4 saat boyunca susuz kalan marul kökleri tamamen kurur ve tüm üretim çöker.',
        'organic_recipe_name': 'Steril Besin Eriyik Aşılaması',
        'organic_recipe_prep': 'Kapalı devre sirkülasyon tankına faydalı Bacillus subtilis bakterileri ve organik kaynaklı aminoasit şelatları eklenir.',
        'organic_recipe_app': 'Besin tankı haftalık olarak analiz edilerek EC/pH dengesi korunur ve faydalı bakteriler suyla sürekli sirküle edilir.',
        'preventative_measures': [
            'Sistemde elektrik kesintilerine karşı mutlaka yedekli jeneratör ve akü grupları bulunmalıdır.',
            'EC ve pH sensörleri haftada bir kez kalibre edilerek besin zehirlenmeleri önlenmelidir.',
            'Kök bölgesinde alg gelişimini önlemek için su kanalları 100% ışık geçirmez yapılmalıdır.'
        ]
    }
}

previews = {
    'cokerten-hastaligi': 'Fideler aşırı sulanmamalıdır. Tohumlar ekilmeden önce faydalı mikoriza ve Trichoderma içeren bakterilerle aşılanmalı, odun külü tozu ile kaplanarak nem bariyeri oluşturulmalıdır.',
    'yaprak-bitleri': 'Sarı yapışkan tuzaklar kurulmalıdır. Arap sabunu, ezilmiş sarımsak maseratı ve neem yağı (soğuk pres) karışımı solüsyonla rüzgarsız günlerde akşamüstü ilaçlaması yapılmalıdır.',
    'demir-klorozu': 'Toprak pH seviyesini düşürmek için elementel toz kükürt uygulanmalı, şelatlı demir organik sıvı gübre formları doğrudan yapraktan serin saatlerde püskürtülmelidir.',
    'mildiyo-salgini': 'Yapraktan sulama tamamen sonlandırılmalı, damlama sulama sabah gün doğumunda yapılmalıdır. Meyveleri güneşten korumak için mineral bazlı ultra ince kaolin kili püskürtülmelidir.',
    'fusarium-solgunlugu': 'Nadas döneminde şeffaf örtülerle toprak solarizasyonu yapılmalıdır. Aktif dönemde kök bölgesine Trichoderma harzianum içeren mikrobiyal kompost şerbeti uygulanmalıdır.',
    'cicek-burnu-curuklugu': 'Toprak nemini dengede tutmak için organik saman malçı yapılmalı, sulama sensörlerle izlenmelidir. Yapraktan organik kalsiyum şelatı uygulaması yapılmalıdır.',
    'kursuni-kuf': 'Hastalıklı yapraklar hızla budanıp yakılmalıdır. Bitki araları açılarak hava akımı artırılmalıdır. Yapraklara doğal potasyum bikarbonat içeren solüsyonlar püskürtülmelidir.',
    'bakteriyel-kanser': 'Budama makasları her budamadan sonra alkol solüsyonu ile sterilize edilmelidir. Budama işleminin hemen ardından yaraları kapatmak için organik bordo bulamacı uygulanmalıdır.',
    'yaprak-kulleme': 'Doğal ıslanabilir kükürt uygulamaları yapılmalıdır. Süt ve su karışımı (1:9) hazırlanarak yapraklara püskürtülmeli ve doğal antifungal protein tabakası oluşturulmalıdır.',
    'radyasyon-donu': 'Don beklenen geceden önce toprak hafifçe sulanarak ısı tutma kapasitesi artırılmalıdır. Bitki sıralarının üzeri elyaf agrotekstil don örtüleriyle sıkıca örtülmelidir.',
    'kok-bogulmasi': 'Tarla sınırlarına 50-80 cm derinliğinde tahliye kanalları açılmalıdır. Toprak yapısını gevşetmek için sonbaharda yüksek oranda kompost ve organik madde takviyesi yapılmalıdır.',
    'govde-catlaklari': 'Ağaç gövdeleri, birinci dallara kadar su bazlı beyaz plastik boya veya kireç bulamacı ile boyanarak kış güneşi yansıtılmalı, genç fidan gövdeleri hasır çuvallarla sarılmalıdır.'
}

pros_cons = {
    'acik-arazi': {
        'pros': [
            {"title": "Düşük Kurulum Yatırımı (CAPEX)", "desc": "Sera demirleri, camlar, ısıtma veya karmaşık sulama otomasyonları gerekmeyip ilk tesis maliyeti asgari düzeyde kaldığı için kolayca ölçeklenebilir."},
            {"title": "Doğal Aroma ve Kuru Madde Oranı", "desc": "Güneş ışığındaki tam spektrumlu UV ışınları ve rüzgar stresi sayesinde meyvelerde Briks (şeker) derecesi ve aromatik asit birikimi en üst seviyededir."},
            {"title": "Zengin Toprak Mikrobiyomu", "desc": "Canlı topraktaki mikoriza mantarları ve bakteriler, bitkinin doğal bağışıklık sistemini destekler ve sürdürülebilir toprak sağlığını korur."}
        ],
        'cons': [
            {"title": "Klimatik Koşullara Tam Bağımlılık", "desc": "Don dalgaları, aşırı dolu yağışı, fırtına veya kuraklık gibi ekstrem hava olaylarına karşı korumasızdır; bir gecede tüm hasat kaybedilebilir."},
            {"title": "Yoğun Yabani Ot ve Böcek İstilası", "desc": "Açık alanda böceklerin ve yabancı ot tohumlarının rüzgarla taşınması engellenemediği için yoğun ve masraflı mekanik/kimyasal mücadele gerektirir."},
            {"title": "Düşük Su Verimliliği", "desc": "Açık kanallar ve salma sulamada buharlaşma kayıpları inanılmaz düzeydedir; su kıtlığı olan bölgelerde sürdürülebilirliği zayıftır."}
        ]
    },
    'sera-uretimi': {
        'pros': [
            {"title": "Dört Mevsim Kesintisiz Hasat", "desc": "Sera içi sıcaklık ve nem optimize edilebildiğinden, dışarıda kar yağarken dahi piyasaya taze ve düzenli ürün tedarik edilebilir."},
            {"title": "Fiziksel Yalıtım ve Temiz Ürün", "desc": "Sera tülleri ve cam kaplamalar böcek geçişini engellediği için kimyasal pestisit kullanım ihtiyacını %60 ila %80 oranında düşürür."},
            {"title": "Birim Alanda Maksimum Hacim", "desc": "Dikey askılama ipleri ve sık dikim planlaması sayesinde açık tarlalara kıyasla metrekare başına 4-5 kat yüksek hasat alınır."}
        ],
        'cons': [
            {"title": "Ciddi İşletim Maliyetleri (OPEX)", "desc": "Kışın ısıtma sobaları/doğalgaz tüketimi, yazın fan ped soğutması ve otomatik havalandırma sistemleri nedeniyle enerji gideri yüksektir."},
            {"title": "Hızlı Yayılan Mantar Salgınları", "desc": "Hatalı veya yetersiz havalandırmalarda içerideki nem %90\'ı aşarsa külleme ve mildiyö mantarları saatler içinde tüm serayı sarabilir."},
            {"title": "Toprak Tuzlanması ve Yorgunluğu", "desc": "Serada ardı ardına yapılan ekimler ve aşırı gübreleme, toprakta tuz akümülasyonuna ve zamanla çoraklaşmaya yol açar."}
        ]
    },
    'topraksiz-tarim': {
        'pros': [
            {"title": "%95 Su Tasarrufu", "desc": "Kapalı devre sirkülasyon sisteminde su arıtılarak köklere geri verildiğinden, geleneksel sulamaya göre neredeyse hiç su harcanmaz."},
            {"title": "Topraksız Steril Ortam & Hızlı Büyüme", "desc": "Toprak patojenleri, nematodlar veya yabani otlar yoktur. Kökler doğrudan oksijenli besin suyuyla beslendiğinden bitki %50 daha hızlı büyür."},
            {"title": "Metropol Dikey İstifleme", "desc": "Katlı raf sistemleri ve özel LED yetiştirme ışıkları sayesinde kent merkezlerinde üretim yapılarak nakliye ve karbon ayak izi sıfıra indirilir."},
        ],
        'cons': [
            {"title": "Son Derece Yüksek Yatırım (CAPEX)", "desc": "EC/pH sensör donanımları, dozajlama otomasyonu, özel LED grow light lambaları ve yedek jeneratör altyapısı kurulumu son derece pahalıdır."},
            {"title": "Arızalarda Sıfır Tolerans Oranı", "desc": "Su sirkülasyonu sağlayan pompalarda elektrik kesintisi veya tıkanıklık oluşursa, kökler havada açık kaldığı için bitkiler saatler içinde solar ve ölür."},
            {"title": "Dar Ürün Gamı", "desc": "Sadece yapraklı yeşillikler, aromatik otlar ve bazı bodur çilek çeşitleri karlı olarak üretilebilir; tahıl veya kök sebze yetiştirmek ekonomik olarak mantıksızdır."}
        ]
    }
}

def run():
    # Clear existing items to prevent duplicates
    FieldGuideItem.objects.all().delete()
    print("Mevcut rehber kayıtları silindi.")
    
    count = 0
    for slug, val in REHBER_DATA.items():
        recipe_preview = previews.get(slug, "")
        pc = pros_cons.get(slug, {})
        pros = pc.get('pros', [])
        cons = pc.get('cons', [])
        
        item = FieldGuideItem(
            slug=slug,
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
            recipe_preview=recipe_preview,
            pros=pros,
            cons=cons
        )
        item.save()
        count += 1
        print(f"Kayıt eklendi: {item.title}")
        
    print(f"Başarıyla tamamlandı! Toplam {count} ziraat rehber içeriği aktarıldı.")

if __name__ == '__main__':
    run()
