import pytest
from dsa.data_structures.linked_list.linked_list import LinkedList, Node


def test_LinkedList_instance():
    assert LinkedList()


def test_LinkedList_str():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    actual = str(ll)
    expected = "{ bananas } -> { apples } -> NULL"
    assert actual == expected


def test_LinkedList_head():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert actual == expected


def test_LinkedList_insert_empty():
    ll = LinkedList()
    ll.insert("apples")
    assert ll.head.value == "apples"


def test_LinkedList_insert_full():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value == "apples"


def test_node_exception():
    with pytest.raises(TypeError):
        Node("ugh", "this is NOT a Node")
