import pytest
import time
from tester_ch_07_12_24.page_object_pattern.pages.google_search import SearchPage
from tester_ch_07_12_24.page_object_pattern.pages.google_results import ResultPage
from selenium import webdriver

@pytest.fixture
def driver():
    # inicjalizacja przegladarki Chrome, zwyczajowa nazwa driver, ale moze byc jakakolwiek
    driver = webdriver.Chrome()
    yield driver # wykonaj to co poza dekoratorem i wroc
    driver.quit()

# test (musi zaczynac sie od test)
def test_google_search(driver): # najpierw pojdzie do funkcji driver

    # stworzenie obiektu klasy SearchPage
    search_page = SearchPage(driver)
    search_page.open()

    assert "Google" in driver.title

    search_page.accept_cookies()

    search_page.search("Pogoda")

    # zatrzymanie skryptu na X sekund, tu akurat obchodzimy zabezpieczenie
    time.sleep(25)

    # stworzenie obiektu klasy ResultPage
    result_page = ResultPage(driver)

    # sprawdzenie czy wyniki wyswietlily sie na stronie
    results = result_page.get_results()

    assert len(results) > 0, "Niestety, nic nie ma" # po przecinku mozna dodac rezultat jak asercja nie przejdzie
    print("dlugosc listy:", len(results))