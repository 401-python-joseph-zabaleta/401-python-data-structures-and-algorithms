import pytest
from dsa.data_structures.tree.tree import (
    Node,
    BinaryTree,
    BinarySearchTree
)

def test_BST_exists():
    assert BinaryTree()


def test_BST_single_root():
    bst = BinarySearchTree()
    bst.add(1337)
    actual = bst.root.value
    expected = 1337
    assert actual == expected

def test_BST_left_and_right():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(1)
    bst.add(3)
    right = bst.root.right.value
    expected_right = 3
    left = bst.root.left.value
    expected_left = 1
    assert right == expected_right
    assert left == expected_left

def test_BST_pre_order():
    bst = BinarySearchTree()
    bst.add(1)
    bst.add(3)
    bst.add(20)
    bst.add(7)
    bst.add(8)
    actual = bst.pre_order()
    expected = [1, 3, 20, 7, 8]
    assert actual == expected

def test_BST_pre_order_2():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(7)
    bst.add(8)
    bst.add(6)
    bst.add(3)
    bst.add(2)
    bst.add(4)
    actual = bst.pre_order()
    expected = [5, 3, 2, 4, 7, 6, 8]
    assert actual == expected

def test_BST_in_order():
    bst = BinarySearchTree()
    bst.add(85)
    bst.add(70)
    bst.add(75)
    bst.add(45)
    bst.add(100)
    bst.add(90)
    bst.add(110)
    actual = bst.in_order()
    expected = [45, 70, 75, 85, 90, 100, 110]
    assert actual == expected

def test_BST_in_order_2():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(60)
    bst.add(55)
    bst.add(40)
    bst.add(45)
    actual = bst.in_order()
    expected = [40, 45, 50, 55, 60]
    assert actual == expected

def test_BST_post_order():
    bst = BinarySearchTree()
    bst.add(85)
    bst.add(70)
    bst.add(75)
    bst.add(45)
    bst.add(100)
    bst.add(90)
    bst.add(110)
    actual = bst.post_order()
    expected = [45, 75, 70, 90, 110, 100, 85]
    assert actual == expected

def test_BST_post_order_2():
    bst = BinarySearchTree()
    bst.add(50)
    bst.add(60)
    bst.add(55)
    bst.add(40)
    bst.add(45)
    actual = bst.post_order()
    expected = [45, 40, 55, 60, 50]
    assert actual == expected

def test_BST_contains_True():
    bst = BinarySearchTree()
    bst.add(85)
    bst.add(70)
    bst.add(75)
    bst.add(45)
    bst.add(100)
    bst.add(90)
    bst.add(110)
    actual = bst.contains(45)
    expected = True
    assert actual == expected

def test_BST_contains_False():
    bst = BinarySearchTree()
    bst.add(85)
    bst.add(70)
    bst.add(75)
    bst.add(45)
    bst.add(100)
    bst.add(90)
    bst.add(110)
    actual = bst.contains(200)
    expected = False
    assert actual == expected
