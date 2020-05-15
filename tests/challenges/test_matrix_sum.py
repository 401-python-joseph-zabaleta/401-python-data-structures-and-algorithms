import pytest
from dsa.challenges.matrix_sum.matrix_sum import matrix_sum

def test_matrix_sum(matrix):
    assert matrix_sum(matrix)

def test_matrix_sum_output_1(matrix):
    actual = matrix_sum(matrix)
    expected = [6, 15, 18]
    assert actual == expected

def test_matrix_sum_output_2(second_matrix):
    actual = matrix_sum(second_matrix)
    expected = [6, 5, 20]
    assert actual == expected

# PyTest Fixtures
@pytest.fixture
def matrix():
    return [ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]

@pytest.fixture
def second_matrix():
    return [ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ]
