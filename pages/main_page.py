from pages.base_page import BasePage
from pages.second_frame import SecondFrame


class MainPage(BasePage):
    def __init__(self, driver, url, timeout=10):
        super().__init__(driver, timeout)
        self.url = url
        self.second_frame = SecondFrame(driver, timeout)

    def open(self):
        super().open(self.url)
