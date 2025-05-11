import unittest 
import random
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
    
    def click_button(self, symbol):
        symbol = str(symbol)
        button = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.XPATH, f"//*[@content-desc='Przycisk {symbol}']")) 
        ) 
        button.click()

    # 2 + 2 = 4
    def test_calculator(self):

        for i in '+-*/':

            for _ in range(2):
                a = random.randint(0, 99)
                b = random.randint(0, 99)

                print(f'Wykonuję działanie: {a} {i} {b} = ?')

                buttons = 'C' + str(a) + str(i) + str(b) + '='

                for button in buttons:
                    print(f'Clicking button: {button}')
                    self.click_button(button)

                equation_text = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[contains(@text, '{a}{i}{b}')]")) 
                )
                self.assertTrue(equation_text.is_displayed())
                
                # Oczekiwanie na pojawienie się tekstu z wynikiem i weryfikacja, czy zawiera on oczekiwany wynik
                result_text = WebDriverWait(self.driver, 10).until( 
                    EC.presence_of_element_located((By.XPATH, "//*[contains(@text, 'Wynik:')]")) 
                )

                self.assertTrue(result_text.is_displayed())
                print(result_text.text)

                # Wyciągnięcie wyniku z tekstu
                # W przypadku dzielenia przez 0, zapisz wynik jako tekst błędu
                # W przeciwnym razie, przekształć wynik na float
                if b == 0 and (i == '/'):
                    displayed_result_flt = result_text.text
                else:
                    displayed_result_flt = float(result_text.text.split("Wynik: ")[1])

                if i == '+':
                    actual_result = float(a + b)
                elif i == '-':
                    actual_result = float(a - b)
                elif i == '*':
                    actual_result = float(a * b)
                elif i == '/':
                    if b != 0:
                        actual_result = float(a / b)
                    else:
                        actual_result = 'Wynik: Błąd dzielenia przez 0'
                else:
                    actual_result = 'Nieznany operator'

                self.assertEqual(displayed_result_flt, actual_result)
        
    def test_dzielenie_przez_0(self):
        pass

    def tearDown(self): 
        if self.driver: 
            self.driver.quit() 
 
if __name__ == '__main__': 
    unittest.main() 