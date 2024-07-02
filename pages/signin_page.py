from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):
    EMAIL_FIELD_NAME = (By.CSS_SELECTOR, "input[id='email-2']")
    PASSWORD_FIELD_NAME = (By.CSS_SELECTOR, "input[id='field']")
    SUBMIT_BUTTON = (By.XPATH, "//a[@wized='loginButton']")
    VERIFY_SIGNIN_HEADER = (By.CSS_SELECTOR, "h1[class*='form-header']")
    VERIFY_LOGIN_NAME = (By.XPATH, "//div[@wized='userName']")
    #AVATAR = (By.CSS_SELECTOR, "div[wized*='totalPageProperties']")

    def verify_signin_page(self):
        self.verify_text('Sign in or create new account', *self.VERIFY_SIGNIN_HEADER)

    def input_field(self, text):
        self.input_text(text, *self.EMAIL_FIELD_NAME)

    def password_field(self, text):
        self.input_text(text, *self.PASSWORD_FIELD_NAME)
        #sleep(1)


    def click_submit_login(self):
        self.click(*self.SUBMIT_BUTTON)
        #self.wait_until_visible(*self.AVATAR)
        sleep(7)




    def verify_user_loggedin(self, expected_name):
        self.verify_partial_text(expected_name, *self.VERIFY_LOGIN_NAME)

        #sleep(3)