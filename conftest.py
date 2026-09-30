from __future__ import annotations

import pytest
from selenium import webdriver


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--url",
        action="store",
        default="https://practice-automation.com/iframes/",
        help="URL of the page under test.",
    )
    parser.addoption(
        "--browser",
        action="append",
        choices=("chrome", "firefox", "edge"),
        default=None,
        help="Browser to run (repeat to select several); defaults to Chrome and Firefox.",
    )


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if "driver" not in metafunc.fixturenames:
        return

    browsers = metafunc.config.getoption("--browser") or ["chrome", "firefox"]
    metafunc.parametrize("driver", browsers, indirect=True, ids=browsers)


@pytest.fixture
def url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--url").rstrip("/") + "/"


@pytest.fixture
def saucedemo_url() -> str:
    return "https://www.saucedemo.com/"


@pytest.fixture
def driver(request: pytest.FixtureRequest):
    driver_factories = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "edge": webdriver.Edge,
    }
    browser_driver = driver_factories[request.param]()
    browser_driver.implicitly_wait(0)
    try:
        browser_driver.maximize_window()
        yield browser_driver
    finally:
        browser_driver.quit()
