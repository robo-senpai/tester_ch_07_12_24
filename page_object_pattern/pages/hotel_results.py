class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.hotel_list_xpath = '//h4[contains(@class, "list_title")]'

    def get_hotel_names(self):
        hotels = self.driver.find_elements('xpath', self.hotel_list_xpath)
        hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
        return hotel_names
