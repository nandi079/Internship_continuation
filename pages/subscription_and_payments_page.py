from selenium.webdriver.common.by import By
from pages.base_page import Page


class SubscriptionAndPaymentsPage(Page):
    SUB_PAY_OPTION = (By.XPATH, "//div[@class='setting-text' and text()= 'Subscription & payments']")
    VERIFY_SUB_PAY = (By.XPATH, "//*[text() = 'Subscription & payments']")
    UPGRADE_PLAN = (By.XPATH, "//a[@wized='upgradePlanButton']")
    BACK_BUTTON = (By.XPATH, "//a[@class='button-verify margin-top-8 white w-inline-block']")

    def click_on_subscription_and_payments(self):
        self.click(*self.SUB_PAY_OPTION)

    def verify_accurate_page_opens(self):
        self.verify_url("https://soft.reelly.io/subscription")

    def verify_title_subscription_and_payments(self):
        self.verify_partial_text('Subscription & payments',*self.VERIFY_SUB_PAY)

    def verify_upgrade_plan_and_back_buttons(self):
        self.wait_until_visible(*self.UPGRADE_PLAN)
        self.verify_text('Upgrade plan', *self.UPGRADE_PLAN)
        self.wait_until_visible(*self.BACK_BUTTON)
        self.verify_text('<- Back', *self.BACK_BUTTON)
