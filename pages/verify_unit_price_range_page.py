from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerifyUnitPriceRangePage(Page):
    VERIFY_UNIT = (By.XPATH, "//div[@class='project-block']")
    FROM_INPUT = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    TO_INPUT = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTER = (By.XPATH, "//a[@wized='applyFilterButtonMLS']")
    VERIFY_CARDS = (By.XPATH, "//div[@class='listing-card']")
    VERIFY_RANGE = (By.XPATH, "//div[@class='number-price-text']")

    def add_price_range_from_unit(self):
        self.wait_until_visible(*self.VERIFY_UNIT)
        self.clear_element(*self.FROM_INPUT)
        self.input_text('1200000', *self.FROM_INPUT)
        self.clear_element(*self.TO_INPUT)
        self.input_text('2000000', *self.TO_INPUT)
        self.wait_until_clickable_click(*self.APPLY_FILTER)

    def verify_all_cards_inside_range(self):
        all_videos = self.find_elements(*self.VERIFY_CARDS)

        for video in all_videos:
            title = video.find_element(*self.VERIFY_RANGE).text
            print(title)
            title = title.replace('AED ', '')
            title = title.replace(',', '', 2)
            print(title)
            assert 1200000 <= int(title) <= 2000000, "Card not in Range!"



