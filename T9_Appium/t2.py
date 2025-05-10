import datetime 
import unittest 
from appium import webdriver 
from appium.options.android import UiAutomator2Options 
from appium.webdriver.common.appiumby import AppiumBy 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
class MyApplicationTests(unittest.TestCase): 
    def setUp(self): 
        options = UiAutomator2Options() 
        options.platform_name = 'Android' 
        options.device_name = 'emulator-5554'  # Zmień na nazwę Twojego urządzenia lub emulatora 
        options.app_package = 'com.example.myapplication'  # Zaktualizuj nazwę pakietu aplikacji 
        options.app_activity = '.MainActivity'  # Zaktualizuj nazwę aktywności, jeśli jest inna 
        options.automation_name = 'UiAutomator2' 
 
        self.driver = webdriver.Remote('http://localhost:4723', options=options) 
 
    def test_display_current_date(self): 
        # Pobieranie aktualnej daty w odpowiednim formacie 
        expected_date = datetime.date.today().strftime("%Y-%m-%d")
        print(f'Oczekiwana data: ', expected_date)
 
        simple_button = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.XPATH, "//*[@content-desc='Prosty Przycisk']")) 
        ) 
        simple_button.click() 
 
        # Oczekiwanie na pojawienie się tekstu z datą i weryfikacja, czy zawiera on oczekiwaną datę 
        date_text = WebDriverWait(self.driver, 5).until( 
            EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, '{expected_date}')]")) 
        ) 
        self.assertTrue(date_text.is_displayed()) 
        self.assertIn(expected_date, date_text.text) 
        print(date_text.text)

    def test_display_current_time(self):
        expected_time = datetime.datetime.now() - datetime.timedelta(hours=2) # na telefonie jest 2h wcześniej
        print(f'Oczekiwana godzina: ', expected_time)
        time_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@content-desc='Przycisk Godziny']"))
        )
        time_button.click()
        
        # Oczekiwanie na pojawienie się tekstu z godziną i weryfikacja, czy zawiera on oczekiwaną godzinę
        time_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, 'Aktualna godzina:')]"))
        )
        self.assertTrue(time_text.is_displayed())
        print(time_text.text)

        # Wyciągnięcie godziny z tekstu
        displayed_time_str = time_text.text.split("Aktualna godzina: ")[1]
        print(f"Godzina w telefonie: ", displayed_time_str)
        time_str = displayed_time_str.split(":")
        print(f"Lista z czasu: ", time_str)

        now = datetime.datetime.now()

        # sprawdzenie, czy godzina w telefonie jest mniej więcej zgodna z oczekiwaną
        # porównać należy timestamp, a nie tylko godzinę ze względu na możliwą różnicę w dniach
        displayed_time_phone = now.replace(hour=int(time_str[0]), minute=int(time_str[1]), second=int(time_str[2]))
        print(f"Timestamp skompilowany z godziny w telefonie: ", displayed_time_phone)
        time_difference = abs((displayed_time_phone - expected_time).total_seconds()) # na wypadek, gdyby różnica była ujemna
        print(f"Różnica w sekundach: ", time_difference)
        self.assertLessEqual(time_difference, 10) # tolerancja 10 sekund
 
    def tearDown(self): 
        if self.driver: 
            self.driver.quit() 
 
if __name__ == '__main__': 
    unittest.main() 