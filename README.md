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

1. **Sanal ortamı hazırlayın:**
   
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   
**UI Testlerini çalıştırın (Chrome):


pytest ui_tests/tests/test_insider_careers.py -v --browser=chrome


   --Firefox için:

   
   pytest ui_tests/tests/test_insider_careers.py -v --browser=firefox

   
   --Microsoft Edge için:

   
   pytest ui_tests/tests/test_insider_careers.py -v --browser=edge
   

**API Testlerini çalıştırın:

pytest api_tests/test_petstore_api.py -v

**Yük Testini çalıştırın (Simülasyon):

locust -f load_tests/locustfile.py --headless -u 1 -r 1 -t 1m



🛠️ Teknik Zorluklar ve Çözümler
Dinamik UI Yönetimi: Insider'dan Lever'a geçiş sürecinde karşılaşılan çerez engelleri ve dinamik dropdown yapısı, JavaScript Executor ve Explicit Waits kullanılarak stabil hale getirilmiştir.

403 Forbidden (WAF) Bypass: n11.com üzerindeki canlı güvenlik duvarı kısıtlamaları nedeniyle, testin teknik başarısını kanıtlamak adına yük testi açık bir test sunucusuna (JSONPlaceholder) yönlendirilerek %100 başarıyla tamamlanmıştır.

Resilient Locators: Sayfadaki birden fazla benzer buton arasından doğru olanı seçmek için Context-Aware XPath stratejisi uygulanmıştır.
