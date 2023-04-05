import pytest
from playwright.sync_api import Playwright

from PageObject.models.main_page import MainPage
from resources import SEARCH_TEXT, GOOGLE_URL, GOOGLE_TITLE


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page):
    page = MainPage(page)
    page.go_to_google(GOOGLE_URL, GOOGLE_TITLE)
    page.search_text(SEARCH_TEXT)
    yield


@pytest.fixture(scope="session", autouse=True)
def page(playwright: Playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    yield page
    browser.close()
