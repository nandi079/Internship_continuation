from selenium.webdriver.common.by import By
from pages.base_page import Page


class UserGuideVideosOptionPage(Page):
    USER_GUIDE_LINK = (By.XPATH, "//div[@class='setting-text' and text()= 'User guide']")
    RIGHT_PAGE_TAB_VERIFY = (By.XPATH, "//div[@class='next-event-text' and text()= 'User guide']")
    VERIFY_VIDEOS_TITLE_LINK = (By.XPATH, "//a[@class='ytp-title-link yt-uix-sessionlink']")

    def user_guide_option(self):
        self.click(*self.USER_GUIDE_LINK)

    def verify_right_page_tab(self):
        self.verify_text('User guide', *self.RIGHT_PAGE_TAB_VERIFY)

    def verify_lesson_videos_titles(self):
        all_videos = self.find_elements(*self.VERIFY_VIDEOS_TITLE_LINK)

        for video in all_videos:
            title = video.find_element(*self.VERIFY_VIDEOS_TITLE_LINK).text
            assert title, 'Full overview of Reelly platform'


