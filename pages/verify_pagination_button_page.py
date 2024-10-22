from pages.base_page import Page
from selenium.webdriver.common.by import By


class VerifyPaginationButtonPage(Page):
    SECONDARY_PAGE = (By.XPATH, "//div[@class='menu-button-text' and text()='Secondary']")
    VERIFY_SECONDARY_PAGE = (By.XPATH, "//div[@class='page-title listing' and text()='Listings']")
    #PAGE_COUNT = (By.XPATH, "[wized='nextPageMLS']")
    #FINAL_PAGE = (By.XPATH, "//div[@class='page-count' and text()='99']")
    #FIRST_PAGE = (By.XPATH, "//div[@wized='currentPageProperties' and text()='1']")
    BACK_BTN = (By.XPATH, "//div[@wized='previousPageMLS']")
    FWD_BTN = (By.XPATH, "//a[@wized='nextPageMLS' and @class='pagination__button w-inline-block']")
    TOTAL_PAGES = (By.XPATH, "//div[@wized='totalPageProperties' and @class='page-count']")
    CUR_PAGE = (By.XPATH, "//div[@wized='currentPageProperties' and @class='page-count']")

    def secondary_option_menu(self):
        self.wait_until_clickable_click(*self.SECONDARY_PAGE)

    def verify_secondary_page(self):
        self.verify_text('Listings', *self.VERIFY_SECONDARY_PAGE)

    def final_pagination_page(self):
        self.wait_until_visible(*self.TOTAL_PAGES)

        PG_COUNT = int(self.find_element(*self.TOTAL_PAGES).text)

        for j in range(PG_COUNT):
            self.wait_until_visible(*self.TOTAL_PAGES)
            self.driver.execute_script("window.scrollBy(0,6000)", "")
            PG = int(self.find_element(*self.CUR_PAGE).text)

            if PG < PG_COUNT:
                self.click(*self.FWD_BTN)

        assert PG == PG_COUNT,"Final page should be 99"

    def first_page_using_pagination_button(self):
        PG_COUNT = int(self.find_element(*self.TOTAL_PAGES).text)

        for j in range(PG_COUNT):
            self.wait_until_visible(*self.TOTAL_PAGES)
            self.driver.execute_script("window.scrollBy(0,6000)", "")
            PG = int(self.find_element(*self.CUR_PAGE).text)

            if PG > 1:
                self.click(*self.BACK_BTN)

        assert PG == 1, "First page should be 1"





