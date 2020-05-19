import pytest
from dsa.data_structures.linked_list.linked_list import LinkedList, Node


def test_LinkedList_instance():
    assert LinkedList()


def test_LinkedList_str():
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    actual = str(ll)
    expected = "{ b } -> { a } -> NULL"
    assert actual == expected


def test_LinkedList_repr():
    ll = LinkedList()
    actual = repr(ll)
    expect = "LinkedList: None"
    assert actual == expect


def test_LinkedList_head():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected


def test_LinkedList_insert():
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    assert ll.head.value == "b"
    assert ll.head.next.value == "a"


def test_LinkedList_includes_true():
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
    actual = ll.includes("c")
    expected = True
    assert actual == expected


def test_LinkedList_includes_false():
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
    actual = ll.includes("d")
    expected = False
    assert actual == expected


def test_node_exception():
    with pytest.raises(TypeError):
        Node("Test", "This must be a node not a string")


@pytest.fixture
def prep():
    """Sets up a linked list instance along with adds a few nodes for testing"""
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
