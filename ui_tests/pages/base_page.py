from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        # Sayfayı kaydırırken elementi ekranın ortasına al (yapışkan header/footer engeline karşı)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        try:
            element.click() # Normal tıklamayı dene
        except ElementClickInterceptedException:
            # Eğer çerez (cookie) vb. bir şey üstünü kapatıyorsa JS ile bypass ederek tıkla
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def switch_to_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        
    def accept_cookies_if_present(self):
        # Yaygın cookie butonlarını bul ve eğer ekrandaysa tıkla
        cookie_locators = [
            (By.ID, "wt-cli-accept-all-btn"),
            (By.XPATH, "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]"),
            (By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept')]")
        ]
        for loc in cookie_locators:
            try:
                # 3 saniye bekle, bulursa tıkla ve döngüden çık
                btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(1)
                break
            except TimeoutException:
                continue
