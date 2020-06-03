import pytest
from dsa.challenges.tree_expanded_find_maximum.tree_expanded_find_maximum import (
    BinaryTree,
    BinarySearchTree
)

def test_BinaryTree_maximum_empty():
    with pytest.raises(ValueError):
        tree = BinaryTree()
        tree.find_maximum()

def test_BinaryTree_maximum_one():
    tree = BinaryTree()
    tree.add(10)
    tree.add(7)
    tree.add(37)
    tree.add(34)
    actual = tree.find_maximum()
    expected = 37
    assert actual == expected

def test_BinaryTree_maximum_two():
    tree = BinaryTree()
    tree.add(22)
    tree.add(55)
    tree.add(14)
    tree.add(76)
    actual = tree.find_maximum()
    expected = 76
    assert actual == expected

def test_BST_maximum_empty():
    with pytest.raises(ValueError):
        bst = BinarySearchTree()
        bst.find_maximum()

def test_BST_maximum_one():
    bst = BinarySearchTree()
    bst.add(87)
    bst.add(1)
    bst.add(27)
    bst.add(18)
    bst.add(99)
    bst.add(2)
    actual = bst.find_maximum()
    expected = 99
    assert actual == expected

def test_BST_maximum_two():
    bst = BinarySearchTree()
    bst.add(48)
    bst.add(13)
    bst.add(27)
    bst.add(2)
    bst.add(54)
    bst.add(22)
    actual = bst.find_maximum()
    expected = 54
    assert actual == expected

