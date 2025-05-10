import unittest 
from appium import webdriver 
from appium.options.android import UiAutomator2Options 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
 
class MyApplicationTests(unittest.TestCase): 
    def setUp(self): 
        options = UiAutomator2Options() 
        options.platform_name = 'Android' 
        options.device_name = 'emulator-5554'  # Zmień na nazwę Twojego urządzenia lub emulatora 
        options.app_package = 'com.example.myapplication2'  # Zaktualizuj nazwę pakietu aplikacji 
        options.app_activity = '.MainActivity'  # Zaktualizuj nazwę aktywności, jeśli jest inna 
        options.automation_name = 'UiAutomator2' 
 
        self.driver = webdriver.Remote('http://localhost:4723', options=options) 
 
    def test_click_something(self): 
        keyboard_displayed = WebDriverWait(self.driver, 5).until( 
            EC.presence_of_element_located((By.XPATH, "//*[contains(@text, 'Wynik:')]"))
        )
        self.assertTrue(keyboard_displayed.is_displayed())

    def tearDown(self): 
        if self.driver: 
            self.driver.quit() 
 
if __name__ == '__main__': 
    unittest.main() 