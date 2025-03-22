from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# inicjalizacja przegladarki Chrome, zwyczajowa nazwa driver, ale moze byc jakakolwiek
driver = webdriver.Chrome()

url = "https://www.google.com"

# przejscie pod konkretny adres w otwartej przegladarce
driver.get(url)

# rozmiar okna; dla testowania lepiej ustalic staly rozmiar okna zamiast maksymalizacji
driver.maximize_window()

# lokalizowanie przycisku akceptacji cookies
accept_cookies = driver.find_element("id", "L2AGLb")

# klikniecie przycisku
accept_cookies.click()

# znajdz pole wyszukiwania, tym razem po name, ale po ID tez mozna
search_field = driver.find_element("name", "q")

# wprowadz haslo w to pole
search_field.send_keys("pogoda")

# kliknij enter
#search_field.send_keys(Keys.ENTER)

# alternatywnie potwierdzenie bez uzycia tej biblioteki
search_field.submit()

# zatrzymanie skryptu na X sekund
time.sleep(5.0)

driver.quit()