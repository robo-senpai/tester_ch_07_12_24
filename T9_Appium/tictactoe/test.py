import unittest 
from appium import webdriver 
from appium.options.android import UiAutomator2Options 
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from time import sleep
 
class MyApplicationTests(unittest.TestCase): 
    def setUp(self): 
        options = UiAutomator2Options() 
        options.platform_name = 'Android' 
        options.device_name = 'emulator-5554'  # Zmień na nazwę Twojego urządzenia lub emulatora 
        options.app_package = 'com.example.apptictactoe'  # Zaktualizuj nazwę pakietu aplikacji 
        options.app_activity = '.StartActivity'  # Zaktualizuj nazwę aktywności, jeśli jest inna 
        options.automation_name = 'UiAutomator2' 
 
        self.driver = webdriver.Remote('http://localhost:4723', options=options)
    
    def test_new_game_button(self):
        # Oczekiwanie na załadowanie przycisku z contentDescription 'Nowa Gra' 
        new_game_button = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.ID, 'com.example.apptictactoe:id/newGameButton')) 
        )

        self.driver.save_screenshot("ekran_startowy.png")

        new_game_button.click()

        sleep(2)

        self.driver.save_screenshot("ekran_nowej_gry.png")
        current_activity = self.driver.current_activity
        self.assertEqual(current_activity, ".MainActivity")

        cell_button = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.ID, 'com.example.apptictactoe:id/button4')) 
        )
        cell_button.click()
        sleep(2)
        self.driver.save_screenshot("ekran_gry_po_wstawieniu_X_srodek.png")
        self.assertEqual(cell_button.text, "X")

    def tearDown(self): 
        if self.driver: 
            self.driver.quit() 
 
if __name__ == '__main__': 
    unittest.main() 