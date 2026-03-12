Bu depo, Senior QA Engineer pozisyonu teknik değerlendirmesi için hazırlanan uçtan uca (end-to-end) test otomasyon projesini içermektedir. UI, API ve Yük testleri modüler ve sürdürülebilir bir yapıda kurgulanmıştır.

## 🏗️ Mimari ve Teknoloji Yığını
* **Dil:** Python 3.9+
* **UI Otomasyonu:** Selenium WebDriver + Pytest (Page Object Model)
* **API Testleri:** Python Requests + Pytest
* **Yük Testi:** Locust
* **Sürücü Yönetimi:** WebDriver Manager

## 📁 Proje Yapısı
* `ui_tests/`: Insider kariyer sayfası ve Lever başvuru akışı otomasyonu.
* `api_tests/`: Petstore API üzerinden CRUD operasyonları doğrulaması.
* `load_tests/`: Arama modülü için performans ve yük simülasyonu.
* `requirements.txt`: Proje bağımlılıkları.

## 🚀 Kurulum ve Çalıştırma
1. Sanal ortamı hazırlayın:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt