from pages.add_project_settings_page import AddProjectSettingsPage
from pages.changing_language_page import ChangingLanguagePage
from pages.community_page import CommunityPage
from pages.connect_the_company_page import ConnectTheCompanyPage
from pages.main_page import MainPage
from pages.signin_page import SignInPage
from pages.subscription_and_payments_page import SubscriptionAndPaymentsPage
from pages.support_option_page import SupportOptionPage
from pages.user_change_password_page import UserChangePasswordPage
from pages.user_guide_videos_option_page import UserGuideVideosOptionPage
from pages.verify_12_setting_options_page import Verify12SettingOptionsPage
from pages.verify_pagination_button_page import VerifyPaginationButtonPage


class Application:
    def __init__(self, driver):
        self.add_project_settings_page = AddProjectSettingsPage(driver)
        self.changing_language_page = ChangingLanguagePage(driver)
        self.connect_the_company_page = ConnectTheCompanyPage(driver)
        self.community_page = CommunityPage(driver)
        self.main_page = MainPage(driver)
        self.signin_page = SignInPage(driver)
        self.subscription_and_payments_page = SubscriptionAndPaymentsPage(driver)
        self.support_option_page = SupportOptionPage(driver)
        self.user_change_password_page = UserChangePasswordPage(driver)
        self.user_guide_videos_option_page = UserGuideVideosOptionPage(driver)
        self.verify_12_setting_options_page = Verify12SettingOptionsPage(driver)
        self.verify_pagination_button_page = VerifyPaginationButtonPage(driver)








