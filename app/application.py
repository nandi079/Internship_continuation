from pages.add_project_settings_page import AddProjectSettingsPage
from pages.changing_language_page import ChangingLanguagePage
from pages.community_page import CommunityPage
from pages.connect_the_company_page import ConnectTheCompanyPage
from pages.main_page import MainPage
from pages.signin_page import SignInPage


class Application:
    def __init__(self, driver):
        self.add_project_settings_page = AddProjectSettingsPage(driver)
        self.changing_language_page = ChangingLanguagePage(driver)
        self.connect_the_company_page = ConnectTheCompanyPage(driver)
        self.community_page = CommunityPage(driver)
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)










