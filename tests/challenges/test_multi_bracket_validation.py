import pytest
from dsa.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

@pytest.mark.skip()
def test_mbv_exists():
    assert multi_bracket_validation('test')

@pytest.mark.skip()
def test_mbv_three_pairs():
    string = '()[]{}'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected


def test_mbv_split():
    string = '(som)thing[inside]{here}'
    actual = multi_bracket_validation(string)
    expected = [1]
    assert actual == expected
