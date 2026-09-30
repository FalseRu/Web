from pages.main_page import MainPage


def test_python_stable_download_link(driver, url):
    page = MainPage(driver, url)
    page.open()

    download_url = page.second_frame.get_python_stable_download_url()

    assert download_url == "https://pypi.python.org/pypi/selenium"
