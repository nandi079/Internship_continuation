from selenium.webdriver.common.by import By
from pages.base_page import Page


class Verify12SettingOptionsPage(Page):
    VERIFY_CMB = (By.XPATH, "//div[@wized = 'clientModeButton']")
    VERIFY_12set = (By.XPATH, "//a[@class = 'page-setting-block w-inline-block']")
    VERIFY_COMPANY_PAGE = (By.XPATH, "//div[@class='get-free-period menu' and text()= 'Connect the company']")

    def verification_12_options(self):
        self.wait_until_visible(*self.VERIFY_CMB)

        all_listing_icons = self.find_elements(*self.VERIFY_12set)
        count_options = len(all_listing_icons)
        assert count_options == 12

    def verify_connect_comp_button(self):
        title = self.find_element(*self.VERIFY_COMPANY_PAGE).text
        assert title, 'Connect the company'
