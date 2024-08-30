from selenium.webdriver.common.by import By
from pages.base_page import Page


class UserChangePasswordPage(Page):
    CHANGE_PASSWORD = (By.XPATH, "//div[@class='setting-text' and text()= 'Change password']")
    VERIFY_SET_NEW_PASSWORD_PAGE = (By.XPATH, "//div[@class='change-password-text' and text()= 'Change password']")
    SET_NEW_PASSWORD = (By.CSS_SELECTOR, "input[id='Enter-new-password']")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[id='Repeat-password']")
    VERIFY_CHAN_PASSWORD_BUTTON = (By.XPATH, "//a[@class='submit-button-2 w-button' and text()= 'Change password']")

    def change_password(self):
        self.click(*self.CHANGE_PASSWORD)

    def verify_change_password_page_opens(self):
        self.verify_text('Change password', *self.VERIFY_SET_NEW_PASSWORD_PAGE)

    def add_new_password(self):
        self.clear_element(*self.SET_NEW_PASSWORD)
        self.input_text('Pythonsetpassword$7$', *self.SET_NEW_PASSWORD)
        self.clear_element(*self.REPEAT_PASSWORD)
        self.input_text('Pythonsetpassword$7$', *self.REPEAT_PASSWORD)

    def verify_change_password_button(self):
        self.verify_partial_text('Change password',*self.VERIFY_CHAN_PASSWORD_BUTTON)


