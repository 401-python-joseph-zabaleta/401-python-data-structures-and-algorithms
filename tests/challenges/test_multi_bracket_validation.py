import pytest
from dsa.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_mbv_exists():
    assert multi_bracket_validation('test')

def test_mbv_three_pairs():
    string = '()[]{}'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == True
