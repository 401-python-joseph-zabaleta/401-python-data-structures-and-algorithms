import pytest
from dsa.challenges.merge_sort.merge_sort import (
    merge_sort,
)

def test_sample_array():
    alist = [8,4,23,42,16,15]
    merge_sort(alist)
    expected = [4, 8, 15, 16, 23, 42]
    assert alist == expected

def test_reversed_sorted_array():
    alist = [20, 18, 12, 8, 5, -2]
    merge_sort(alist)
    expected = [-2, 5, 8, 12, 18, 20]
    assert alist == expected

def test_few_uniques_array():
    alist = [5,12,7,5,5,7]
    actual = merge_sort(alist)
    expected = [5, 5, 5, 7, 7, 12]
    assert alist == expected

def test_nearly_sorted_array():
    alist = [2,3,5,7,13,11]
    actual = merge_sort(alist)
    expected = [2, 3, 5, 7, 11, 13]
    assert alist == expected
