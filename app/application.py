from pages.main_page import MainPage
from pages.signin_page import SignInPage
from pages.task4_page import Task4Page

class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)
        self.task4_page = Task4Page(driver)
