from selenium.webdriver.common.by import By
from pages.base_page import Page


class AddProjectSettingsPage(Page):
    ADD_PROJECT_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()='Add a project']")
    VERIFY_ADD_PRJ_PG = (By.XPATH,"//div[@class='h2-text book']")
    VERIFY_PAGE = (By.XPATH, "//div[@wized='userName' and text()='test+nandini+careerist']")
    NAME_FIELD = (By.CSS_SELECTOR, "input[id='Your-name']")
    COMPANY_NAME = (By.CSS_SELECTOR, "input[id='Your-company-name']")
    ROLE_FIELD = (By.CSS_SELECTOR, "input[id='Role']")
    COMPANY_AGE = (By.CSS_SELECTOR, "input[id='Age-of-the-company']")
    COUNTRY_PRO_PLACING = (By.CSS_SELECTOR, "input[id='Country']")
    PRO_NAME = (By.CSS_SELECTOR, "input[id='Name-project']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[id='Phone']")
    EMAIL_ID = (By.CSS_SELECTOR, "input[id='Email-add-project']")
    VERIFY_SEND_APPLICATION = (By.XPATH, "//input[@class='purchase-access w-button' and @value='Send an application']")
    SEND_APPLICATION_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def click_on_add_project(self):
        self.wait_until_clickable_click(*self.ADD_PROJECT_BUTTON)

    def verify_right_page(self):
        self.verify_partial_text('Add your project',*self.VERIFY_ADD_PRJ_PG)

    def test_information_fields(self):
        self.wait_until_visible(*self.VERIFY_PAGE)
        self.verify_text('test+nandini+careerist', *self.VERIFY_PAGE)
        self.clear_element(*self.NAME_FIELD)
        self.input_text('Nandini', *self.NAME_FIELD)
        self.clear_element(*self.COMPANY_NAME)
        self.input_text('HCLTech', *self.COMPANY_NAME)
        self.clear_element(*self.ROLE_FIELD)
        self.input_text('QA Engineer', *self.ROLE_FIELD)
        self.clear_element(*self.COMPANY_AGE)
        self.input_text('25', *self.COMPANY_AGE)
        self.clear_element(*self.COUNTRY_PRO_PLACING)
        self.input_text('India', *self.COUNTRY_PRO_PLACING)
        self.clear_element(*self.PRO_NAME)
        self.input_text('QA Technology', *self.PRO_NAME)
        self.clear_element(*self.PHONE_NUMBER)
        self.input_text('123-449-779', *self.PHONE_NUMBER)
        self.clear_element(*self.EMAIL_ID)
        self.input_text('abc95@gmail.com', *self.EMAIL_ID)

    def verify_right_information(self):
        self.verify_entered_text('Nandini', *self.NAME_FIELD)
        self.verify_entered_text('HCLTech', *self.COMPANY_NAME)
        self.verify_entered_text('QA Engineer', *self.ROLE_FIELD)
        self.verify_entered_text('25', *self.COMPANY_AGE)
        self.verify_entered_text('India', *self.COUNTRY_PRO_PLACING)
        self.verify_entered_text('QA Technology', *self.PRO_NAME)
        self.verify_entered_text('123-449-779', *self.PHONE_NUMBER)
        self.verify_entered_text('abc95@gmail.com', *self.EMAIL_ID)

    def verify_application_available_and_clickable(self):
        self.wait_until_visible(*self.SEND_APPLICATION_BUTTON)
        self.verify_entered_text('Send an application',*self.VERIFY_SEND_APPLICATION)
        self.wait_until_clickable_click(*self.VERIFY_SEND_APPLICATION)
