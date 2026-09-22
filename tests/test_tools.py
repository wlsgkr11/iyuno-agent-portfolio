from app.tools import calculator


def test_calculator_addition():
    assert calculator("10 + 5") == 15


def test_calculator_multiplication():
    assert calculator("120 * 0.15") == 18


def test_calculator_division():
    assert calculator("100 / 4") == 25


def test_calculator_subtraction():
    assert calculator("20 - 8") == 12


def test_calculator_invalid_expression():
    result = calculator("hello")

    assert "계산 오류" in result or "허용되지 않은 문자" in result