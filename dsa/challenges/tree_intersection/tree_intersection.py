from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        """Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance."""
        self.storage.appendleft(value)

    def dequeue(self):
        """Takes no arguments, remove the node from the front of the queue, and returns the node's value."""
        return self.storage.pop()

    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        return self.storage[-1]

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return len(self.storage) == 0


def tree_intersection(root1, root2):
    """Takes two binary tree roots and will return a list of intersecting values, or nodes that share the same value at the same position in the tree.
    """
    output = []
    collection1 = []
    collection2 = []

    tree1 = Queue()
    tree1.enqueue(root1.root)
    while not tree1.is_empty():
        front = tree1.dequeue()
        collection1.append(front.value)

        if front.left:
            tree1.enqueue(front.left)

        if front.right:
            tree1.enqueue(front.right)

    tree2 = Queue()
    tree2.enqueue(root2.root)
    while not tree2.is_empty():
        front = tree2.dequeue()
        collection2.append(front.value)

        if front.left:
            tree2.enqueue(front.left)

        if front.right:
            tree2.enqueue(front.right)

    if len(collection1) > len(collection2):
        for i in range(len(collection2)):
            if collection1[i] == collection2[i]:
                output.append(collection1[i])
    else:
        for i in range(len(collection1)):
            if collection1[i] == collection2[i]:
                output.append(collection1[i])

    return output
