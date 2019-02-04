import pytest
from number_to_word import number_to_word


def test_valid_string():
    assert number_to_word.number_to_word("111") == 'one hundred eleven'


def test_invalid_string():
    with pytest.raises(ValueError):
        number_to_word.number_to_word("not a number")


def test_int():
    assert number_to_word.number_to_word(111) == 'one hundred eleven'


def test_float():
    assert number_to_word.number_to_word(111.0) == 'one hundred eleven'


def test_decimal_places():
    assert number_to_word.number_to_word(.999) == 'zero point nine nine nine'


def test_minus_int():
    assert number_to_word.number_to_word(-1) == 'minus one'


def test_minus_float():
    assert number_to_word.number_to_word(-1.01) == 'minus one point zero one'


def test_zero():
    assert number_to_word.number_to_word(0) == 'zero'


def test_bigger_than_max():
    with pytest.raises(AssertionError):
        number_to_word.number_to_word(10**30)
