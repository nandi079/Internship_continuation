from pages.base_page import Page
from selenium.webdriver.common.by import By


class SupportOptionPage(Page):
    SUPPORT_BUTTON_OPTION = (By.XPATH, "//div[@class='setting-text' and text()= 'Support']")
    NEW_PAGE_OPEN = 'https://api.whatsapp.com/send?phone=971568098349&text=Please%20describe%20your%20problem%20or%20ask%20a%20question.%0A%0A'
    NEWS_OPTION_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()= 'News']")

    def click_support_button(self):
        self.click(*self.SUPPORT_BUTTON_OPTION)

    def switch_new_tab_page(self):
        self.switch_to_new_window()

    def verify_support_page_open(self):
        self.verify_url('https://api.whatsapp.com')

    def go_back_to_setting_page(self):
        self.open('https://soft.reelly.io/settings')
        #all_windows = self.driver.window_handles  # window1,2,3..
        #print('ALL windows:', self.driver.window_handles)
        #print('switching to ...', all_windows[0])  # use index [0] to return to first window
        #self.driver.switch_to.window(all_windows[0])

    def click_news_button(self):
        self.click(*self.NEWS_OPTION_BUTTON)

    def verify_news_page_open(self):
        self.verify_url('https://t.me')










