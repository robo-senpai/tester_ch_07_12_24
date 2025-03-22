from docutils.frontend import validate_encoding_and_error_handler
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# inicjalizacja przegladarki Chrome, zwyczajowa nazwa driver, ale moze byc jakakolwiek
driver = webdriver.Chrome()

# oczekiwanie na pojawienie sie kazdego elementu na stronie przez max X sekund
# driverr.implicitly_wait(5)

url = "https://www.w3schools.com/"

# przejscie pod konkretny adres w otwartej przegladarce
driver.get(url)

# rozmiar okna; dla testowania lepiej ustalic staly rozmiar okna zamiast maksymalizacji
driver.maximize_window()

time.sleep(3)
# lokalizowanie przycisku akceptacji cookies
accept_cookiess = driver.find_element("id", "accept-choices")

# klikniecie przycisku
accept_cookiess.click()

# nawigacja do tutorials za pomoca jednej linijki (mniej czytelne)
# driverr.find_element("id", "navbtn_tutorials").click()

menu = driver.find_element("id", "navbtn_tutorials")

# action chains - przydatne do interakcji z elementami typu podwojny klik, scroll, drag drop itp.
# perform - czasem sam klik nie wystarczy
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# otwarcie tutoriali HTML
learnhtml = driver.find_element('xpath','//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
learnhtml.click()

# explicitly wait - czekamy na konkretny element
wait = WebDriverWait(driver, 10, 0.5)

# warunek oczekiwania
# wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))
# gdyby byl problem to mozna uzyc starej metody
# wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftmenuinnerinner"]/a[43])))

# warunek wlasny: oczekiwanie na to az find elements (czyli lista, w ktorej python zapisze znalezione elementy) bedzie tru, czyli >0
wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[71]')))
# ogolnie lepiej uzywac tych wbudowanych, ale mozna tez tak

# otwarcie menu tag list
menuTagList = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[71]')
menuTagList.click()

# menu 'input'
menuInput = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/div/a[59]')
menuInput.click()

# click 'disabled'
driver.find_element('xpath', '//*[@id="main"]/table[2]/tbody/tr[8]/td[1]/a').click()

# kliknij 'try it yourself'
driver.find_element('xpath', '//*[@id="main"]/div[2]/a').click()

# dowod, ze nadal jestesmy w pierwszej zakladce
print("Aktualne okno: ", driver.title)

# przelaczamy na zakladke z inputem
# obecna zakladka
currentTab = driver.current_window_handle

# lista wszystkich zakladek (okienek)
allTabs = driver.window_handles

# sprawdzic w petli czy dana zakladka nie jest aktualna, a jak nie to przelaczamy
for window in allTabs:
    if window != currentTab:
        driver.switch_to.window(window)

print("Przejscie do zakladki: ", driver.title)

# strona osadzona w specjalnej ramce - zeby w niej dzialac, trzeba do niej przejsc
driver.switch_to.frame(driver.find_element('id', 'iframeResult'))

# wprowadzenie imienia
nameInput = driver.find_element('xpath', '//*[@id="fname"]')
nameInput.send_keys("Robo")

print("Wprowadzono imie.")

# wprowadzenie nazwiska, ktore jest disabled

lastnameInput = driver.find_element('xpath', '//*[@id="lname"]')

if lastnameInput.is_enabled():
    lastnameInput.send_keys("Kropka")
    print("Wprowadzono nazwisko.")
else:
    print("Nie mozna wprowadzic nazwiska.")

time.sleep(2)

driver.close()

driver.switch_to.window(currentTab)
print("Aktualne okno: ", driver.title)

# cofniecie w przegladarce
driver.back()

# link 'checked'
linkChecked = driver.find_element('xpath', '//*[@id="main"]/table[2]/tbody/tr[6]/td[1]/a')
linkChecked.click()

# kliknij 'try it yourself'
driver.find_element('xpath', '//*[@id="main"]/div[2]/a').click()

print("Aktualne okno: ", driver.title)

# przelaczamy na zakladke z inputem
# obecna zakladka
currentTab = driver.current_window_handle

# lista wszystkich zakladek (okienek)
allTabs = driver.window_handles

# sprawdzic w petli czy dana zakladka nie jest aktualna, a jak nie to przelaczamy
for window in allTabs:
    if window != currentTab:
        driver.switch_to.window(window)

print("Przejscie do zakladki: ", driver.title)

# strona osadzona w specjalnej ramce - zeby w niej dzialac, trzeba do niej przejsc
driver.switch_to.frame(driver.find_element('id', 'iframeResult'))

# zaznaczenie checkboxa mam samochod
optionCar = driver.find_element('name', 'vehicle2')

# jak sprawdzic czy cos jest zaznaczone
if optionCar.is_selected():
    print("Opcja 2 jest zaznaczona.")
else:
    print("Opcja 2 nie jest zaznaczona.")
    optionCar.click()
    print("Zaznaczono opcje 'Mam samochod'.")

# ponowne uruchomienie testu nadpisze plik
# jak maja byc unikalne to warto uzyc random albo timestampa
# mozna zapisywac tylko jak sie uda albo wywali
# przy wielu testach warto pomyslec o innego rodzaju logach zamiast robic screeny co kazdy krok
driver.save_screenshot("zakonczenie_testu.png")

time.sleep(3)

driver.quit()