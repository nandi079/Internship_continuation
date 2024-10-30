from selenium.webdriver.common.by import By
from pages.base_page import Page


class VerifyAllCardProductsPage(Page):
    VERIFY_SEC_PAGE = (By.XPATH, "//a[@href='/my-secondary-listings' and text()='My listings']")
    CLK_FILTER = (By.XPATH, "//div[@class='filter-text' and text()='Filters']")
    CLICK_WTS = (By.XPATH, "//div[@class='tag-text-filters' and text()='Want to sell']")
    CLICK_APPLY_FILTER = (By.XPATH, "//a[@wized='applyFilterButtonMLS' and text()='Apply filter']")
    VERIFY_SALE_TAG = (By.XPATH, "//div[@wized='saleTagMLS' and text()='For sale']")

    def verification_sec_page(self):
        self.verify_text('My listings', *self.VERIFY_SEC_PAGE)

    def click_on_filters_button(self):
        self.wait_until_clickable_click(*self.CLK_FILTER)

    def click_on_want_to_sell(self):
        self.click(*self.CLICK_WTS)
        self.wait_until_clickable_click(*self.CLICK_WTS)

    def click_on_apply_filter_button(self):
        self.click(*self.CLICK_APPLY_FILTER)

    def verify_all_card_for_sale(self):
        all_listing = self.find_elements(*self.VERIFY_SALE_TAG)

        for listing in all_listing:
            title = listing.find_element(*self.VERIFY_SALE_TAG).text
            print(title)
            assert title, 'For sale'





