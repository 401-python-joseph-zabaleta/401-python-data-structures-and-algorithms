import pytest
from dsa.challenges.queue_with_stacks.queue_with_stacks import (
    Node,
    Stack,
    PseudoQueue
)

# Tests Instances
def test_Node_exists():
    assert Node("test")

def test_Stack_exists():
    assert Stack()

def test_PseudoQueue_exists():
    assert PseudoQueue()

# Queue Tests

def test_PseudoQueue_enqueue_one_item():
    my_queue = PseudoQueue()
    my_queue.enqueue(1)
    actual = str(my_queue.storage1)
    expected = "[1] -> NULL"
    assert actual == expected

def test_PseudoQueue_enqueue_multiple_items():
    my_queue = PseudoQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    actual = str(my_queue.storage1)
    expected = "[3] -> [2] -> [1] -> NULL"
    assert actual == expected

def test_PseudoQueue_dequeue_one_item():
    my_queue = PseudoQueue()
    my_queue.enqueue(1)
    my_queue.dequeue()
    actual = str(my_queue.storage1)
    expected = "NULL"
    assert actual == expected

def test_PseudoQueue_dequeue_multiple_items():
    my_queue = PseudoQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.dequeue()
    my_queue.dequeue()
    actual = str(my_queue.storage1)
    expected = "[3] -> NULL"
    assert actual == expected
