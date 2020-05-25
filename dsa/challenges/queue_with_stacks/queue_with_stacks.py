class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"

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
        try:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.value
        except AttributeError:
            return "Can't pop item from an empty stack"

    def peek(self):
        """Takes no arguments and returns the value of the node located on top of the stack, without removing it from the stack."""
        try:
            return self.top.value
        except AttributeError:
            return "Can't peek top from an empty stack"

    def is_empty(self):
        """Takes no arguments, and returns a boolean indicating whether or not the stack is empty."""
        return not bool(self.top)

class PseudoQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        output = ""
        current = self.front
        while current:
            output += f"{[ current.value ]} -> "
            current = current.next
        return output + "NULL"

    def enqueue(self, item):
        """Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance."""
        if self.rear == None:
            self.front = Node(item)
            self.rear = self.front
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next

    def dequeue(self):
        """Takes no arguments, remove the node from the front of the queue, and returns the node's value."""
        try:
            removed = self.front
            self.front = self.front.next
            return removed.value
        except AttributeError:
            return "Can't dequeue from an empty queue"
