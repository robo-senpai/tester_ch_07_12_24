import pytest
import time
from tester_ch_07_12_24.page_object_pattern.pages.hotel_search import SearchHotelPage
from tester_ch_07_12_24.page_object_pattern.pages.hotel_results import SearchResultPage
from selenium import webdriver

class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get('http://www.kurs-selenium.pl/demo')
        search_page = SearchHotelPage(self.driver)
        search_page.set_city("Dubai")
        search_page.set_dates("23/03/2025", "24/03/2025")
        search_page.set_travellers(1, 2)
        search_page.perform_search()