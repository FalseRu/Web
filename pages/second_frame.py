from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SecondFrame(BasePage):
    frame = (By.ID, "iframe-2")
    downloads_link = (By.LINK_TEXT, "Downloads")
    downloads_heading = (By.XPATH, "//h1[normalize-space()='Downloads']")
    python_stable_link = (
        By.XPATH,
        "//a[contains(@href, 'pypi.python.org/pypi/selenium')]",
    )

    def get_python_stable_download_url(self):
        self.switch_to_default_content()
        self.switch_to_frame(self.frame)
        self.click(self.downloads_link)
        self.find_visible(self.downloads_heading)
        return self.find_visible(self.python_stable_link).get_attribute("href")
