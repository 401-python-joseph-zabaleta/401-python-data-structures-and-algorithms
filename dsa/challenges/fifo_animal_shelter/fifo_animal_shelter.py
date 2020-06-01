class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    def __init__(self, item=None):
        self.top = item

    def push(self, item):
        """Takes in any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance."""
        if self.top == None:
            self.top = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """Takes no arguments, removes the node from the top of the stack, and returns the node's value."""
        if not self.top:
            raise AttributeError("Can't pop item from an empty stack")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value

    def peek(self):
        """Takes no arguments and returns the value of the node located on top of the stack, without removing it from the stack."""
        if not self.top:
            raise AttributeError("Can't peek top from an empty stack")
        return self.top.value

    def is_empty(self):
        """Takes no arguments, and returns a boolean indicating whether or not the stack is empty."""
        return not bool(self.top)

class PseudoQueue:
    def __init__(self):
        self.storage1 = Stack()
        self.storage2 = Stack()

    def enqueue(self, animal):
        """Takes in an animal object argument and adds that value to the back of the queue."""
        self.storage1.push(animal)

    def dequeue(self, pref=None):
        """Takes in a preference of animal to remove and removes them from the front of the queue."""

        if pref == None or pref not in ['cat', 'dog']:
            return None

        current = self.storage1.top

        while current:
            self.storage2.push(current.value)
            current = current.next
        # self.storage2.pop()

        self.storage1 = Stack()

        current = self.storage2.top
        while current:
            if current.value.kind == pref:
                removed = self.storage2.pop()
            else:
                self.storage1.push(current.value)
            current = current.next

        self.storage2 = Stack()
        return removed


class Dog:
    def __init__(self, name):
        self.name = name
        self.kind = 'dog'

class Cat:
    def __init__(self, name):
        self.name = name
        self.kind = 'cat'

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):
        """Takes in an animal object argument and adds that value to the back of the queue."""
        if self.rear == None:
            self.front = Node(animal)
            self.rear = self.front
        else:
            self.rear.next = Node(animal)
            self.rear = self.rear.next

    def dequeue(self, pref=None):
        """Takes in a preference of animal to remove and removes them from the front of the queue."""
        if not self.front:
            raise AttributeError("Can't dequeue from an empty queue")

        if pref == None or pref not in ['cat', 'dog']:
            return None

        if self.front.value.kind == pref:
            removed = self.front
            self.front = self.front.next
            return removed.value.kind
        else:
            return f"A {pref} is not first in line."


    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        if not self.front:
            raise AttributeError("Can't peek from an empty queue")
        return self.front.value

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return not bool(self.front)

