from selenium.webdriver.common.keys import Keys

class SearchPage:
    def __init__(self, driver): # init - konstruktor
        self.driver = driver
        self.accept_cookies_button = ("id", "L2AGLb")
        self.search_box = ("name", "q")

    def open(self):
        self.driver.get("https://google.com")

    def accept_cookies(self):
        accept_cookies = self.driver.find_element(*self.accept_cookies_button) # * rozpakowanie krotki, zeby wkleily sie wszystkie elementy a nie jako 1
        accept_cookies.click()

    def search(self, query):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)
