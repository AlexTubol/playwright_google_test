"""Описание страницы калькулятора"""
from playwright.sync_api import Page

from components.models.calculator import Calculator
from page.models.base_page import BasePage


class CalculatorSearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.calculator = Calculator(page)

    @property
    def type_page(self) -> str:
        return 'calculator page'
