"""Описание главной страницы."""
import re

from playwright.sync_api import expect

from PageObject.models.base_page import BasePage


class MainPage(BasePage):
    SEARCH_BOX = "Найти"

    def source_field(self):
        source_field = self.page.get_by_role(role="combobox", name=self.SEARCH_BOX)
        expect(source_field).to_be_empty()
        return source_field

    def search_text(self, text: str):
        """
        Полученный текст вводить в поисковое поле
        Проверяет корректность полученной поисковой страницы через title.
        """
        search_text = self.source_field()
        search_text.fill(text)
        search_text.press("Enter")
        return expect(self.page).to_have_title(re.compile(text))

    def go_to_google(self, url: str, title: str):
        self.go_to_page(url)
        return expect(self.page).to_have_title(title)
