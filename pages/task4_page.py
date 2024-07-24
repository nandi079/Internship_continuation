from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from time import sleep

class Task4Page(Page):
    MAIN_MENU_LINK = (By.XPATH, "//div[@class='menu-button-text' and text()='Main menu']")
    EDIT_LANGUAGE = (By.XPATH, "//a[@tabindex ='0' and text()='RU']")
    CHANGE_LANGUAGE = (By.CSS_SELECTOR, "[id='w-dropdown-toggle-0']")
    VERIFY_LANGUAGE = (By.XPATH, "//h1[@class='h1-menu' and text()='Главное меню']")

    def click_on_main_menu(self):
        self.wait_until_clickable_click(*self.MAIN_MENU_LINK)

    def click_on_language_page(self):
        self.click(*self.CHANGE_LANGUAGE)
        self.wait_until_clickable_click(*self.CHANGE_LANGUAGE)
        self.click(*self.EDIT_LANGUAGE)

    def verify_the_language(self):
        #self.verify_text('Главное меню', *self.CHANGE_LANGUAGE)
        all_listing = self.find_elements(*self.VERIFY_LANGUAGE)

        for listing in all_listing:
            title = listing.find_element(*self.VERIFY_LANGUAGE).text
            assert title, 'RU'#'Главное меню'

















