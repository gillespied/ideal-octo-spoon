from number_to_word import number_to_word
# run the tests required by the assessor.


def test_111():
    assert number_to_word.number_to_word(111) == 'one hundred eleven'


def test_4032():
    assert number_to_word.number_to_word(4032) == 'four thousand thirty two'


def test_87413():
    assert number_to_word.number_to_word(87413) == 'eighty seven thousand four hundred thirteen'


def test_45p2():
    assert number_to_word.number_to_word(45.2) == 'forty five point two'

