from selenium import webdriver
import time

# inicjalizacja przegladarki Chrome, zwyczajowa nazwa driver, ale moze byc jakakolwiek
driver = webdriver.Chrome()

url = "https://www.google.com"
url2 = "https://www.wp.pl"

# przejscie pod konkretny adres w otwartej przegladarce
driver.get(url)

# rozmiar okna; dla testowania lepiej ustalic staly rozmiar okna zamiast maksymalizacji
driver.maximize_window()

# dobrze zrobic staly rozmiar, zapisac jako zmienne w, h czy cos
# driver.set_window_size(1080, 768)

# otwarcie nowej zakladki, z uzyciem JS
driver.execute_script("window.open('');")

# driver.get(url2) poskutkuje otwarciem nowego adresu w tej samej zakladce, a nie nowej
# tak samo driver.close() zamknie pierwsza zakladke, po czym wywali blad na koniec, bo nie bedzie wiedzial, co ma zamknac (juz zamknal)

# przelaczenie drivera do drugiej zakladki
# okna sa przechowywane w liscie
driver.switch_to.window(driver.window_handles[1]) # okno o indeksie 1

driver.get(url2)

# zatrzymanie skryptu na X sekund
time.sleep(5.0)

# zamkniecie przegladarki: quit (cala przegladarka) lub close (jeden tab)
driver.close()
time.sleep(3.0)
driver.quit()