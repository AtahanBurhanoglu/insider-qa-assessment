from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
import time

class QACareersPage(BasePage):
    SEE_ALL_TEAMS_BTN = (By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'see all teams')] | //a[text()='See all teams']")
    
    # Akraba/Hiyerarşi bağımsız Sequential XPath:
    QA_SPECIFIC_POSITIONS_BTN = (By.XPATH, "(//*[contains(text(), 'Obsessed with perfection') or contains(text(), 'Quality Assurance')]/following::*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'positions')])[1]")
    
    SEE_ALL_QA_JOBS_BTN = (By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'see all qa jobs')]")

    def go_to(self, url="https://insiderone.com/careers/quality-assurance/"):
        self.driver.get(url)
        self.accept_cookies_if_present()

    def click_see_all_qa_jobs(self):
        # 1. Varsa 'See all teams' alanını genişlet
        try:
            self.click_element(self.SEE_ALL_TEAMS_BTN)
            time.sleep(2)
        except TimeoutException:
            pass

        # 2. Direkt olarak QA departmanının altındaki doğru Positions butonunu hedefle
        try:
            self.click_element(self.SEE_ALL_QA_JOBS_BTN)
        except TimeoutException:
            self.click_element(self.QA_SPECIFIC_POSITIONS_BTN)
            
        time.sleep(3) # AJAX/Yönlendirme toleransı
