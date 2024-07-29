from pages.main_page import MainPage
from pages.signin_page import SignInPage
from pages.changing_language_page import ChangingLanguagePage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)
        self.changing_language_page = ChangingLanguagePage(driver)
