import pytest
import allure

from page.models.calculator import CalculatorSearchPage


@pytest.mark.usefixtures('before_each_calculator_search_page')
class TestCalculatorSearchPage:
    @allure.feature('Calculator - arithmetic operators')
    @allure.story('Проверка выполнения базовых выражений.')
    @allure.severity('critical')
    @pytest.mark.parametrize("expression, result",
                             [("1+2=", "3"),
                              ("1-3=", "-2"),
                              ("1*1=", "1"),
                              ("10/2=", "5")])
    def test_static_data_calculator(self, page, expression, result, calculator_search_page: CalculatorSearchPage):
        calculator_search_page.calculator.checking_the_calculator_result(expression=expression, result=result)

    @allure.feature('Calculator - arithmetic operators')
    @allure.story('Проверка выполнения сгенерериванных выражений')
    @allure.severity('critical')
    def test_dynamic_data_calculator(self, page, test_data, calculator_search_page: CalculatorSearchPage):
        calculator_search_page.calculator.checking_the_calculator_result(expression=test_data[0], result=test_data[1])
