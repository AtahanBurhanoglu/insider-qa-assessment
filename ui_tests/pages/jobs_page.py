from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class JobsPage(BasePage):
    LOCATION_FILTER_BTN = (By.XPATH, "//*[contains(translate(text(), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'LOCATION') and not(contains(translate(text(), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'TYPE'))]")
    
    JOB_LIST = (By.CSS_SELECTOR, ".posting")
    JOB_POSITION = (By.CSS_SELECTOR, "[data-qa='posting-name'], h5")
    APPLY_BTN = (By.XPATH, ".//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'apply')]")
    
    # Yeni Adım İçin Locator: İlan detay sayfasındaki "Apply for this job" butonu
    APPLY_FOR_THIS_JOB_BTN = (By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'apply for this job')] | //a[contains(@class, 'postings-btn')]")

    def filter_jobs(self, location="Istanbul"):
        self.switch_to_new_window()
        time.sleep(3)
        
        try:
            loc_btn = self.wait.until(EC.presence_of_element_located(self.LOCATION_FILTER_BTN))
            self.driver.execute_script("arguments[0].click();", loc_btn)
            time.sleep(2)
            
            loc_option = self.driver.find_element(By.XPATH, f"//a[contains(text(), '{location}')] | //li[contains(text(), '{location}')]")
            self.driver.execute_script("arguments[0].click();", loc_option)
            time.sleep(3)
        except Exception as e:
            print(f"Filtreleme Sirasinda Hata Alindi: {e}")

    def verify_job_list_presence(self):
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(2)
        jobs = self.driver.find_elements(*self.JOB_LIST)
        assert len(jobs) > 0, "Filtreleme sonrasi is ilani bulunamadi."
        return jobs

    def verify_job_details(self, jobs, expected_position, expected_department, expected_location):
        for job in jobs:
            position = job.find_element(*self.JOB_POSITION).text
            full_card_text = job.text 
            
            assert expected_position.lower() in position.lower() or "quality assurance" in position.lower() or "qa" in position.lower(), f"Pozisyon hatali: {position}"
            assert expected_location.lower() in full_card_text.lower() or "turkiye" in full_card_text.lower() or "turkey" in full_card_text.lower(), f"Lokasyon hatali. Beklenen: {expected_location}, Bulunan kart metni: {full_card_text}"

    def click_view_role_and_verify_redirect(self, job_element):
        # 1. Listedeki APPLY butonuna tıkla
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", job_element)
        time.sleep(1)
        btn = job_element.find_element(*self.APPLY_BTN)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(3) # İlan detay sayfasının yüklenmesini bekle
        
        # 2. İlan detay sayfasındaki 'Apply for this job' butonuna tıkla
        try:
            apply_for_job_btn = self.wait.until(EC.presence_of_element_located(self.APPLY_FOR_THIS_JOB_BTN))
            self.driver.execute_script("arguments[0].click();", apply_for_job_btn)
            time.sleep(3) # Başvuru formunun yüklenmesini bekle
        except Exception as e:
            print(f"Apply for this job butonu bulunamadi: {e}")
            
        # 3. Son URL doğrulaması
        assert "jobs.lever.co" in self.driver.current_url and "apply" in self.driver.current_url, "Basvuru formuna yonlendirme basarisiz."
