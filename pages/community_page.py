from pages.base_page import Page
from selenium.webdriver.common.by import By


class CommunityPage(Page):
    COMMUNITY_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()='Community']")
    VERIFY_CONTACT_SUPPORT = (By.XPATH, "//a[@href='/notification' and text()='Contact support']")
    CLICK_CONTACT_SUPPORT = (By.XPATH, "//a[@id='w-node-_746955f8-6d08-524d-7f43-03daaced30ff-7f66deba' and text()='Contact support']")

    def click_community_option(self):
        self.wait_until_clickable_click(*self.COMMUNITY_BUTTON)

    def right_page_verify(self):
        self.verify_url("https://soft.reelly.io/community")

    def verify_contact_support_available_clickable(self):
        all_contacts = self.find_elements(*self.VERIFY_CONTACT_SUPPORT)

        for listing in all_contacts:
            title = listing.find_element(*self.VERIFY_CONTACT_SUPPORT).click()
            print(title)
            assert title, 'Send Message'








