import pytest
from dsa.challenges.ll_merge.ll_merge import LinkedList, Node, merge_list


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


def test_merge_list_list1_none():
    list1 = LinkedList()
    list2 = LinkedList()
    list2.insert("c")
    list2.insert("b")
    list2.insert("a")
    actual = str(merge_list(list1, list2))
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected


def test_merge_list_list2_none():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert("c")
    list1.insert("b")
    list1.insert("a")
    actual = str(merge_list(list1, list2))
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected


def test_merge_list_equal_lists():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert("e")
    list1.insert("c")
    list1.insert("a")
    list2.insert("f")
    list2.insert("d")
    list2.insert("b")
    actual = str(merge_list(list1, list2))
    expected = "{ a } -> { b } -> { c } -> { d } -> { e } -> { f } -> NULL"
    assert actual == expected


def test_merge_list_list1_shorter():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert("3")
    list1.insert("1")
    list2.insert("4")
    list2.insert("9")
    list2.insert("5")
    actual = str(merge_list(list1, list2))
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NULL"
    assert actual == expected


def test_merge_list_list1_longer():
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert("3")
    list1.insert("1")
    list1.insert("4")
    list2.insert("9")
    list2.insert("5")
    actual = str(merge_list(list1, list2))
    expected = "{ 4 } -> { 5 } -> { 1 } -> { 9 } -> { 3 } -> NULL"
    assert actual == expected


@pytest.fixture
def ll_list():
    """Sets up a linked list instance along with adds a few nodes for testing"""
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
    return ll


@pytest.fixture
def ll_list_merge():
    """Sets up two linked list instances along with some nodes for testing"""
    list1 = LinkedList()
    list1.insert("c")
    list1.insert("b")
    list1.insert("a")
