import re

from playwright.sync_api import expect, Page

from components.elements.input import Input
from page.models.base_page import BasePage
from resources import GOOGLE_URL, GOOGLE_TITLE


class MainPage(BasePage):
    SEARCH_BOX = "//*[@type='search']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = Input(page=page, locator=self.SEARCH_BOX, name="search_field", name_page=self.name_page)
        self.url = GOOGLE_URL
        self.title = GOOGLE_TITLE

    @property
    def name_page(self) -> str:
        return 'main page'

    def search_text(self, text: str):
        """
        Полученный текст вводить в поисковое поле
        Проверяет корректность полученной поисковой страницы через title.
        """
        self.search_input.to_be_empty()
        self.search_input.fill(text)
        self.search_input.press("Enter")
        return expect(self.page).to_have_title(re.compile(text))

    def go_to_page(self):
        self.go_to(self.url)
        self.should_have_title(self.title)
