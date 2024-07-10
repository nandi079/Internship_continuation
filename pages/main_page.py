from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage(Page):
    OFF_PLAN_LINK = (By.CSS_SELECTOR, "address[id='w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b']")
    FILTER_LINK = (By.XPATH, "//a[@class='filter-button w-inline-block']")
    NEWLY_LAUNCHED_FILTER = (By.XPATH, "//div[@class='tag-text-proparties'and text()='Newly Launched']")
    NEW_LAUNCHED_LISTING = (By.XPATH, "//div[@w-el-text='Status']")
    LOG_IN = (By.XPATH, "//div[@class='sing-in-text' and text()='Sign in']")
    LOGIN = (By.CSS_SELECTOR, "div[wizard='signinButtonSignup']")
    CONNECT_LINK = (By.XPATH, "//div[@class='get-free-period menu' and text()='Connect the company']")
    CLICK_ON_CONTINUE = (By.CSS_SELECTOR, "a[class='login-button w-button']")
    NEW_TAB = 'https://soft.reelly.io/book-presentation'
    VERIFY_RIGHT_TAB = (By.XPATH, "[class*='popuop-masterclass book']")
    EMAIL_FIELD_NAME1 = (By.CSS_SELECTOR, "input[id='email-2']")
    PASSWORD_FIELD_NAME2 = (By.CSS_SELECTOR, "input[id='field']")

    def __init__(self, driver):
        super().__init__(driver)
        self.CLICK_CONTINUE = None
        self.OPEN_PAGE = None

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def open_main_page(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def login(self):
        self.click(*self.LOG_IN)
        self.input_text('nandinisarkar079@gmail.com', *self.EMAIL_FIELD_NAME1)
        self.input_text('Howrah123$', *self.PASSWORD_FIELD_NAME2)

    def click_on_continue(self):
        #self.click(*self.CLICK_CONTINUE)
        self.click(*self.CLICK_ON_CONTINUE)
    
    def click_on_company(self):
        #self.click(*self.CONNECT_LINK)
        self.wait_until_clickable_click(*self.CONNECT_LINK)
        #sleep(5)

    def switch_new_tab(self):
        self.switch_to_new_window()

    def verify_right_tab(self):
        self.verify_url(*self.NEW_TAB)

    def click_on_text(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_LINK)
        #sleep(5)

    def open_filter_window(self):
        self.wait_until_clickable_click(*self.FILTER_LINK)
        #sleep(3)

    def open_newlaunch_filter(self):
        self.wait_until_clickable_click(*self.NEWLY_LAUNCHED_FILTER)
        #sleep(7)

    def verify_newlaunch_tag(self):
        all_listing = self.find_elements(*self.NEW_LAUNCHED_LISTING)  # [WebEl1, WebEl2, WebEl3, WebEl4]

        for listing in all_listing:
            title = listing.find_element(*self.NEW_LAUNCHED_LISTING).text
            assert title, 'Newly Launched'