# Verda: Bilimsel Ziraat Akademisi & Backend API

Bu repository, **Verda: Yapay Zeka Tabanlı Bitki Hastalıkları Teşhis Sistemi**'nin web yönetim portalını ve mobil uygulamanın kullandığı backend API servislerini barındıran Django projesidir.

---

## 🚀 Öne Çıkan Özellikler

### 🌾 1. Bilimsel Ziraat & Tarla Rehberi
*   **Bento Grid Arayüzü:** Mevsimsel bitki problemlerini tehlike derecelerine göre görselleştiren, fare takipli ışık hüzmesi (spotlight) efektli premium grid tasarımı.
*   **iOS Tarzı Mevsim Değiştirici:** Sayfa yenilenmeden mevsimler arası geçiş sağlayan, her mevsime özel dinamik arka plan küreleri (mesh orbs) barındıran akıcı geçişler.
*   **Canlı Arama & Akıllı Filtreleme:** Hastalık adı, bilimsel adı, risk düzeyi veya kategorisine göre anlık istemci tarafı filtreleme.

### 🧪 2. İnteraktif Laboratuvar Paneli
*   **Klimatik Simülatör Sandbox:** Sıcaklık ve nem sürgüleri (slider) ayarlanarak hastalıkların anlık üreme/büyüme hızını (risk faktörünü) hesaplayan matematiksel simülasyon motoru.
*   **Fitoterapi Sentezleme:** Web Audio API tabanlı pop-sesleri ve CSS animasyonlu kimyasal baloncuk üreteci ile dijital reçete sentezleme deneyimi.
*   **Akademik Teşhis Raporu (`@media print`):** "Bilimsel Rapor Al" butonuyla tarla durum raporunu tüm arayüz butonlarından arındırıp tertemiz bir akademik PDF veya baskı formatına getirme.

### 💻 3. Django REST API ve Mobil Entegrasyon
*   Saha teşhis modeli için görüntü işleme servisleri.
*   Akıllı ziraat danışmanlık sohbet arayüzü (Chatbot) API uçları.
*   Kapsamlı bitki ansiklopedisi ve hastalık veri tabanı API'leri.

---

## 🛠️ Kurulum ve Çalıştırma

1.  **Sanal Ortamı Aktif Edin:**
    ```bash
    python -m venv .venv
    # Windows için:
    .venv\Scripts\activate
    ```
2.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Veritabanı Göçlerini Gerçekleştirin:**
    ```bash
    python manage.py migrate
    ```
4.  **Veri Tabanını Doldurun (Opsiyonel):**
    ```bash
    python manage.py shell < populate_guide_db.py
    ```
5.  **Geliştirme Sunucusunu Başlatın:**
    ```bash
    python manage.py runserver
    ```
    Uygulama yerelde `http://127.0.0.1:8000/` adresinde çalışacaktır. Tarla rehberine `/tarla-rehberi/` adresinden ulaşabilirsiniz.
