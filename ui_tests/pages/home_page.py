from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    NAV_BAR = (By.ID, "navigation")
    
    def go_to(self, url="https://insiderone.com/"):
        self.driver.get(url)
        self.accept_cookies_if_present() # Sayfa açılır açılmaz çerezleri hallet

    def verify_home_page_loaded(self):
        assert self.is_element_displayed(self.NAV_BAR) != None, "Home page blocks are not loaded properly"
