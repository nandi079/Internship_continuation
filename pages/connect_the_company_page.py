from selenium.webdriver.common.by import By
from pages.base_page import Page


class ConnectTheCompanyPage(Page):
    CLICK_CONTACT = (By.XPATH, "//div[@class='setting-text' and text()='Contact us']")
    VERIFYING_PAGE = (By.XPATH, "//a[@href='/book-presentation']")
    INSTAGRAM_LINK = (By.XPATH, "//div[@class='text-social' and text()= 'Instagram']")
    TELEGRAM_LINK = (By.XPATH, "//div[@class='text-social' and text()= 'Telegram']")
    LINKEDIN_LINK = (By.XPATH, "//div[@class='text-social' and text()= 'LinkedIn']")
    WHATSAPP_LINK = (By.XPATH, "//div[@class='text-social' and text()= 'Youtube']")
    VERIFY_COMPANY_PAGE = (By.XPATH, "//div[@class='get-free-period menu' and text()= 'Connect the company']")
    #CLICK_COMPANY_PAGE =(By.XPATH, "//*[text()= 'Connect the company']")
    def click_contact_us(self):
        self.wait_until_clickable_click(*self.CLICK_CONTACT)

    def verify_correct_page_opening(self):
        self.verify_partial_text('',*self.VERIFYING_PAGE)

    def verify_social_media_icons(self):
        self.wait_until_visible(*self.INSTAGRAM_LINK)
        self.verify_text('Instagram', *self.INSTAGRAM_LINK)
        self.wait_until_visible(*self.INSTAGRAM_LINK)
        self.verify_text('Telegram', *self.TELEGRAM_LINK)
        self.wait_until_visible(*self.INSTAGRAM_LINK)
        self.verify_text('LinkedIn', *self.LINKEDIN_LINK)
        self.wait_until_visible(*self.INSTAGRAM_LINK)
        self.verify_text('Youtube', *self.WHATSAPP_LINK)


    def verify_connect_the_company_button_availabe_and_clickable(self):
        all_listing_icons = self.find_elements(*self.VERIFY_COMPANY_PAGE)

        for listing in all_listing_icons:
            title = listing.find_element(*self.VERIFY_COMPANY_PAGE).text
            assert title, 'Connect the company'

