import pytest

from PageObject.models.calculator import GoogleCalculator


@pytest.mark.parametrize("expression, result",
                         [("1+2=", "3"),
                          ("1-3=", "-2"),
                          ("1*1=", "1"),
                          ("10/2=", "5")])
def test_google_calculator(page, expression, result):
    page = GoogleCalculator(page)
    page.check_calculator(expression=expression, result=result)
