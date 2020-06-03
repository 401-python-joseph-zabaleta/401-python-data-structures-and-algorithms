import pytest
from dsa.challenges.tree_expanded_breadth_first.tree_expanded_breadth_first import (
    BinaryTree,
    BinarySearchTree
)

def test_BinaryTree_breadth_example():
    tree = BinaryTree()
    tree.add(2)
    tree.add(7)
    tree.add(5)
    tree.add(2)
    tree.add(6)
    tree.add(9)
    actual = tree.breadth_first()
    expected = [2, 7, 5, 2, 6, 9]
    assert actual == expected

def test_BinaryTree_breadth():
    tree = BinaryTree()
    tree.add(1)
    tree.add(5)
    tree.add(4)
    tree.add(7)
    actual = tree.breadth_first()
    expected = [1, 5, 4, 7]
    assert actual == expected

def test_BinaryTree_breadth_two():
    tree = BinaryTree()
    tree.add(3)
    tree.add(15)
    tree.add(7)
    tree.add(5)
    tree.add(3)
    tree.add(5)
    tree.add(15)
    actual = tree.breadth_first()
    expected = [3, 15, 7, 5, 3, 5, 15]
    assert actual == expected

def test_BST_breadth():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(4)
    bst.add(7)
    bst.add(9)
    bst.add(2)
    bst.add(3)
    actual = bst.breadth_first()
    expected = [5, 4, 7, 2, 9, 3]
    assert actual == expected

def test_BST_breadth_two():
    bst = BinarySearchTree()
    bst.add(7)
    bst.add(3)
    bst.add(9)
    bst.add(4)
    bst.add(2)
    bst.add(5)
    actual = bst.breadth_first()
    expected = [7, 3, 9, 2, 4, 5]
    assert actual == expected
