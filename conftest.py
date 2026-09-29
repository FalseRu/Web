from __future__ import annotations

import pytest
from selenium import webdriver


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--url",
        action="store",
        default="https://www.saucedemo.com/",
        help="Base URL of the shop under test.",
    )
    parser.addoption(
        "--browser",
        action="append",
        choices=("chrome", "firefox", "edge"),
        default=None,
        help="Browser to run (repeat to select several); defaults to Chrome and Firefox.",
    )


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if "browser_name" not in metafunc.fixturenames:
        return

    browsers = metafunc.config.getoption("--browser") or ["chrome", "firefox"]
    metafunc.parametrize("browser_name", browsers, indirect=True, ids=browsers)


@pytest.fixture
def url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--url").rstrip("/") + "/"


@pytest.fixture
def browser_name(request: pytest.FixtureRequest) -> str:
    return request.param


@pytest.fixture
def browser(browser_name: str):
    """Create a WebDriver instance and always close its browser after the test."""
    drivers = {
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        "edge": webdriver.Edge,
    }
    driver = drivers[browser_name]()
    driver.maximize_window()
    yield driver
    driver.quit()
