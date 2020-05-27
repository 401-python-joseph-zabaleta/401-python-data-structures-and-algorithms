import pytest
from dsa.data_structures.ll_kth_from_end.ll_kth_from_end import LinkedList, Node


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


def test_LinkedList_insert_before(ll_list):
    ll_list.insertBefore("a", "d")
    actual = str(ll_list)
    expected = "{ c } -> { b } -> { d } -> { a } -> NULL"
    assert actual == expected


def test_LinkedList_insert_before_false(ll_list):
    with pytest.raises(ValueError):
        ll_list.insertAfter("f", "d")


def test_LinkedList_insert_after(ll_list):
    ll_list.insertAfter("b", "d")
    actual = str(ll_list)
    expected = "{ c } -> { b } -> { d } -> { a } -> NULL"
    assert actual == expected


def test_LinkedList_insert_Exception(ll_list):
    with pytest.raises(ValueError):
        ll_list.insertAfter("f", "d")


def test_LinkedList_includes_true(ll_list):
    actual = ll_list.includes("c")
    expected = True
    assert actual == expected


def test_LinkedList_includes_false(ll_list):
    actual = ll_list.includes("d")
    expected = False
    assert actual == expected


def test_LinkedList_append(ll_list):
    ll_list.append("d")
    actual = str(ll_list)
    expected = "{ c } -> { b } -> { a } -> { d } -> NULL"
    assert actual == expected


def test_LinkedList_kth_from_end_0():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 2
    assert actual == expected


def test_LinkedList_kth_from_end_resubmission_0():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 5
    assert actual == expected


def test_LinkedList_kth_from_end_resubmission_1():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    actual = ll.kth_from_end(1)
    expected = 4
    assert actual == expected


def test_LinkedList_kth_from_end_2():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(2)
    expected = 3
    assert actual == expected


def test_LinkedList_kth_from_end_same_length():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    actual = ll.kth_from_end(2)
    expected = 8
    assert actual == expected


def test_LinkedList_kth_from_end_IndexError_Exception():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    with pytest.raises(IndexError):
        ll.kth_from_end(6)


def test_LinkedList_kth_from_end_ValueError_Exception():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    with pytest.raises(ValueError):
        ll.kth_from_end(-6)


def test_node_exception():
    with pytest.raises(TypeError):
        Node("Test", "This must be a node not a string")


@pytest.fixture
def ll_list():
    """Sets up a linked list instance along with adds a few nodes for testing"""
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
    return ll
