import pytest
from dsa.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_mbv_exists():
    assert multi_bracket_validation('test')

def test_mbv_one():
    string = '{}'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_mbv_two():
    string = '{}(){}'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_mbv_three():
    string = '()[[Extra Characters]]'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_mbv_four():
    string = '(){}[[]]'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_mbv_five():
    string = '{}{Code}[Fellows](())'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_mbv_six():
    string = '[({}]'
    actual = multi_bracket_validation(string)
    expected = False
    assert actual == expected

def test_mbv_seven():
    string = '(]('
    actual = multi_bracket_validation(string)
    expected = False
    assert actual == expected

def test_mbv_eight():
    string = '{(})'
    actual = multi_bracket_validation(string)
    expected = False
    assert actual == expected
