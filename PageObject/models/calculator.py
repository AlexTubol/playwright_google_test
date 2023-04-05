"""Описание страницы калькулятора"""
from playwright.sync_api import expect

from PageObject.models.base_page import BasePage


class GoogleCalculator(BasePage):
    CALCULATOR_FIELD = '//div[@class = "card-section"]//div[@role="presentation"]'

    def check_calculator(self, expression, result):
        """
        Находит поле калькулятора и проверяет, что значение установленно по умолчанию
        Вводит арифметическое выражение, сравнивает с ожидаемым результатом
        Возвращает резултат проверки.
        """
        field = self.calculator_field()
        expect(field).to_contain_text("0")
        field.type(expression)
        return self.check_calculator_result(result)

    def calculator_field(self):
        return self.find_element(self.CALCULATOR_FIELD)

    def check_calculator_result(self, assertion):
        result = self.calculator_field()
        return expect(result).to_contain_text(assertion)
