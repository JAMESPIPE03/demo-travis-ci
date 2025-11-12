from app import sum_numbers


def test_sum_numbers_positive():
    assert sum_numbers(2, 3) == 5


def test_sum_numbers_negative():
    assert sum_numbers(-1, -4) == -5
