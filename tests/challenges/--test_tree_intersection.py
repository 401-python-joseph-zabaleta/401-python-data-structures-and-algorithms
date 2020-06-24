import pytest
from dsa.challenges.tree_expanded_breadth_first.tree_expanded_breadth_first import BinaryTree
from dsa.challenges.tree_intersection.tree_intersection import tree_intersection

def test_BST_exists():
    assert BinaryTree()

def test_example1():
    tree1 = BinaryTree()
    tree1.add(150)
    tree1.add(100)
    tree1.add(250)
    tree1.add(75)
    tree1.add(160)
    tree1.add(200)
    tree1.add(350)
    tree1.add(125)
    tree1.add(175)
    tree1.add(300)
    tree1.add(500)

    tree2 = BinaryTree()
    tree2.add(42)
    tree2.add(100)
    tree2.add(600)
    tree2.add(15)
    tree2.add(160)
    tree2.add(200)
    tree2.add(350)
    tree2.add(125)
    tree2.add(175)
    tree2.add(4)
    tree2.add(500)

    actual = tree_intersection(tree1, tree2)
    expected = [100, 160, 200, 350, 125, 175, 500]
    assert actual == expected

def test_example2():
    tree1 = BinaryTree()
    tree1.add(100)

    tree2 = BinaryTree()
    tree2.add(100)

    actual = tree_intersection(tree1, tree2)
    expected = [100]
    assert actual == expected

def test_example3():
    tree1 = BinaryTree()
    tree1.add(100)
    tree1.add(23)
    tree1.add(55)

    tree2 = BinaryTree()
    tree2.add(77)
    tree2.add(5)
    tree2.add(27)

    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected
