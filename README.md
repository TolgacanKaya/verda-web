# 🌐 VERDA WEB: Intelligent Agronomy Portal & Django REST API Backend

[![Django](https://img.shields.io/badge/Django-5.0%2B-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![REST API](https://img.shields.io/badge/API-Django%20REST%20Framework-red.svg?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**VERDA WEB** is the central backend architecture and web portal of the **VERDA Agricultural Ecosystem**. Built with **Django 5.x** and **Django REST Framework**, it serves as both a high-throughput REST API gateway for mobile AI inference and a feature-rich web administration platform for modern agronomy, disease cataloging, and interactive climate simulation.

---

## 🔗 Ecosystem Architecture

Verda Web is a core component of the three-tier Verda ecosystem:

| Repository | Description | Link |
| :--- | :--- | :--- |
| 🧠 **plant_disease_xai** | Deep Learning models, GrabCut segmentation, and Grad-CAM XAI interpretability engine. | [GitHub Repository](https://github.com/TolgacanKaya/plant_disease_xai) |
| 🌐 **verda-web** | Django REST API server, agronomy encyclopedia, prescription database, and web portal. | [GitHub Repository](https://github.com/TolgacanKaya/verda-web) |
| 📱 **verda-mobile** | Cross-platform Flutter mobile application for field image scanning and TTS remedies. | [GitHub Repository](https://github.com/TolgacanKaya/verda-mobile) |

---

## 🌟 Key Features & Capabilities

### 🌾 1. Interactive Agronomy & Field Guide
* **Bento Grid Layout**: Sleek visual layout categorizing plant pathologies by risk severity, featuring cursor-following spotlight effects and responsive design.
* **iOS-Inspired Season Switcher**: Dynamic, non-reloading seasonal toggle (Spring, Summer, Autumn, Winter) with customized background mesh gradient orbs.
* **Real-time Client Filtering**: Instant search and multi-attribute filtering by disease name, scientific binomial, risk index, or plant category.

### 🧪 2. Interactive Laboratory & Phytotherapy Panel
* **Climatic Risk Simulator**: Dynamic sandbox environment with temperature and humidity controls calculating pathogen reproduction velocity and outbreak probability in real time.
* **Digital Phytotherapy Synthesizer**: Immersive prescription generator leveraging Web Audio API audio cues and CSS bubble particle physics for organic and chemical treatment formulation.
* **Printable Agronomy Certificate (`@media print`)**: One-click generation of clean, print-optimized diagnostic reports devoid of navigation UI.

### 💻 3. Django REST API Gateway
* **Inference Endpoint**: Receives leaf images from mobile clients, triggers OpenCV GrabCut background segmentation, invokes PyTorch neural inference, and returns Grad-CAM heatmaps.
* **Agronomy Encyclopedia API**: Structured JSON endpoints providing plant disease definitions, prevention guidelines, and botanical metadata.
* **Prescription Engine API**: Delivers paired **Organic (Ecological/Biological)** and **Chemical (Fungicide/Pesticide)** recipes based on diagnosed pathology IDs.
* **Community & Discussion Feed**: REST endpoints supporting user diagnostic history, community posts, and agronomist feedback.

---

## 🛠️ Technology Stack

* **Framework**: Django 5.x, Django REST Framework (DRF)
* **Programming Language**: Python 3.10+
* **Database**: SQLite3 (pre-populated with agricultural pathology & prescription data)
* **Frontend Technologies**: HTML5, Vanilla CSS3 (Custom Glassmorphism & Bento Grid design), Modern JavaScript (ES6+)
* **Audio & Visual Effects**: Web Audio API, CSS Animations & Custom Canvas Particles
* **Integration Libraries**: PyTorch runtime bridge, OpenCV (cv2), Pillow, NumPy

---

## 📁 Repository Directory Structure

```
verda-web / ziraat_core/
├── accounts/                  # User management, profiles & authentication API
├── community/                 # User discussion feeds, posts & community views
├── config/                    # Core Django settings, WSGI/ASGI & main URL routing
├── core/                      # Field guide, laboratory simulator & home portal views
├── diagnostics/               # REST API endpoints for AI inference & Grad-CAM visualizer
├── encyclopedia/              # Botanical pathology reference catalog & JSON API
├── field_guide/               # Field guide models, forms & views
├── media/                     # Plant photos, disease covers & processed heatmap artifacts
├── scripts/                   # Database seeding and population scripts
├── templates/                 # Master HTML templates & partial UI components
├── db.sqlite3                 # Pre-populated agronomy & prescription database
└── manage.py                  # Django administrative utility
```

---

## 🚀 Getting Started & Installation

### Prerequisites
* Python 3.10 or higher
* `pip` package manager

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/TolgacanKaya/verda-web.git
cd verda-web

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations

```bash
python manage.py migrate
```

### 4. Seed Database (Optional)

```bash
python manage.py shell < scripts/populate_database.py
```

### 5. Launch Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

* **Web Portal**: Navigate to `http://127.0.0.1:8000/`
* **Field Guide**: Navigate to `http://127.0.0.1:8000/tarla-rehberi/`
* **REST API Endpoints**: `http://127.0.0.1:8000/api/`
* **Admin Dashboard**: `http://127.0.0.1:8000/admin/`

---

## 📜 License

This project is licensed under the MIT License — see the `LICENSE` file for details.
