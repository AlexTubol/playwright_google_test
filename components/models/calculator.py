"""Описание страницы калькулятора"""
from playwright.sync_api import Page

from components.elements.input import Input


class Calculator:
    CALCULATOR_FIELD = '//div[@class = "card-section"]//div[@role="presentation"]'

    def __init__(self, page: Page) -> None:
        self.calculator_field = Input(page=page, locator=self.CALCULATOR_FIELD, name="calculator_field")

    @property
    def type(self) -> str:
        return 'calculator'

    def checking_the_calculator_result(self, expression: str, result: str):
        """
        Находит поле калькулятора и проверяет, что значение установленно по умолчанию
        Вводит арифметическое выражение, сравнивает с ожидаемым результатом.
        """
        self.calculator_field.should_contain_text(text='0')
        self.calculator_field.type(expression)
        self.calculator_field.should_contain_text(text=result)
