from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# inicjalizacja przegladarki Chrome, zwyczajowa nazwa driver, ale moze byc jakakolwiek
driverr = webdriver.Chrome()

# oczekiwanie na pojawienie sie kazdego elementu na stronie przez max X sekund
# driverr.implicitly_wait(5)

url = "https://www.w3schools.com/"

# przejscie pod konkretny adres w otwartej przegladarce
driverr.get(url)

# rozmiar okna; dla testowania lepiej ustalic staly rozmiar okna zamiast maksymalizacji
driverr.maximize_window()

time.sleep(3)
# lokalizowanie przycisku akceptacji cookies
accept_cookiess = driverr.find_element("id", "accept-choices")

# klikniecie przycisku
accept_cookiess.click()

# nawigacja do tutorials za pomoca jednej linijki (mniej czytelne)
# driverr.find_element("id", "navbtn_tutorials").click()

menu = driverr.find_element("id", "navbtn_tutorials")

# action chains - przydatne do interakcji z elementami typu podwojny klik, scroll, drag drop itp.
# perform - czasem sam klik nie wystarczy
webdriver.ActionChains(driverr).move_to_element(menu).click().perform()

# otwarcie tutoriali HTML
learnhtml = driverr.find_element('xpath','//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
learnhtml.click()

# explicitly wait - czekamy na konkretny element
wait = WebDriverWait(driverr, 10, 0.5)

# warunek oczekiwania
# wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))
# gdyby byl problem to mozna uzyc starej metody
# wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftmenuinnerinner"]/a[43])))

# warunek wlasny: oczekiwanie na to az find elements (czyli lista, w ktorej python zapisze znalezione elementy) bedzie tru, czyli >0
wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))
# ogolnie lepiej uzywac tych wbudowanych, ale mozna tez tak

# otwarcie tutorialu input types
input_types = driverr.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')
input_types.click()

time.sleep(5)

driverr.quit()