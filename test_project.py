import pytest
from project import calculate_bmi, classify_bmi


def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == pytest.approx(22.86, 0.01)
    assert calculate_bmi(60, 1.65) == pytest.approx(22.04, 0.01)
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)


def test_classify_bmi():
    assert classify_bmi(17) == "Underweight"
    assert classify_bmi(22) == "Normal weight"
    assert classify_bmi(27) == "Overweight"
    assert classify_bmi(32) == "Obesity"


def test_get_user_input(monkeypatch):
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "70")
    weight, height = get_user_input()
    assert weight == 70
    assert height == 1.75
    