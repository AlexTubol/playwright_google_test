import pytest

from PageObject.models.calculator import GoogleCalculator

"""
Проверка выполнения базовых выражений.
"""


@pytest.mark.parametrize("expression, result",
                         [("1+2=", "3"),
                          ("1-3=", "-2"),
                          ("1*1=", "1"),
                          ("10/2=", "5")])
def test_static_data_calculator(page, expression, result):
    page = GoogleCalculator(page)
    page.check_calculator(expression=expression, result=result)


def test_dynamic_data_calculator(page, test_data):
    page = GoogleCalculator(page)
    page.check_calculator(expression=test_data[0], result=test_data[1])
