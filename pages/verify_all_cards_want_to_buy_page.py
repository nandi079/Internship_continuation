from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerifyAllCardsWantToBuyPage(Page):
    CLICK_WTB = (By.XPATH, "//div[@class='tag-text-filters' and text()='Want to buy']")
    VERIFY_ALL_CARDS = (By.XPATH, "//div[@wized='listingCardMLS']")
    VERIFY_BUY_TAG = (By.XPATH, "//div[@wized='saleTagMLS' and text()='Want to buy']")

    def click_on_want_to_buy(self):
        self.click(*self.CLICK_WTB)
        self.wait_until_clickable_click(*self.CLICK_WTB)

    def verify_all_card_want_to_buy(self):
        all_listing = self.find_elements(*self.VERIFY_ALL_CARDS)
        print(all_listing)

        for listing in all_listing:
            title = listing.find_element(*self.VERIFY_BUY_TAG).text
            print(title)
            assert title, 'Want to buy not present'





