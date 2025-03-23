import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # inicjalizacja przegladarki Chrome, zwyczajowa nazwa driver, ale moze byc jakakolwiek
    driver = webdriver.Chrome()
    yield driver # wykonaj to co poza dekoratorem i wroc
    driver.quit()

# test (musi zaczynac sie od test)
def test_google_search(driver): # najpierw pojdzie do driver
    # adres strony do otwarcia
    url = "https://www.google.com"

    # przejscie pod konkretny adres w otwartej przegladarce
    driver.get(url)

    assert "Google" in driver.title

    # lokalizowanie przycisku akceptacji cookies
    accept_cookies = driver.find_element("id", "L2AGLb")

    # klikniecie przycisku
    accept_cookies.click()

    # znajdz pole wyszukiwania, tym razem po name, ale po ID tez mozna
    search_field = driver.find_element("name", "q")

    # wprowadz haslo w to pole
    search_field.send_keys("pogoda")

    # kliknij enter
    search_field.send_keys(Keys.ENTER)

    # alternatywnie potwierdzenie bez uzycia tej biblioteki
    # search_field.submit()

    # zatrzymanie skryptu na X sekund, tu akurat obchodzimy zabezpieczenie
    time.sleep(15)

    # nie dziala 'normalne' wyszukanie jak po xpath z uzyciem css selector
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    # sprawdzenie czy wyniki wyswietlily sie na stronie
    assert len(results) > 0, "Niestety, nic nie ma" # po przecinku mozna dodac rezultat jak asercja nie przejdzie
    print("dlugosc listy:", len(results))