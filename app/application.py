from pages.main_page import MainPage
from pages.signin_page import SignInPage
from pages.changing_language_page import ChangingLanguagePage
from pages.add_project_settings_page import AddProjectSettingsPage
from pages.community_page import CommunityPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)
        self.changing_language_page = ChangingLanguagePage(driver)
        self.add_project_settings_page = AddProjectSettingsPage(driver)
        self.community_page = CommunityPage(driver)







