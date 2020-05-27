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

    def __str__(self):
        output = ""
        current = self.top
        while current:
            output += f"{ [current.value]} -> "
            current = current.next
        return output + "NULL"

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

    def enqueue(self, item):
        """Takes any value as an argument and adds a new node with that value to the back of the queue."""
        self.storage1.push(item)

    def dequeue(self):
        """Takes no arguments, remove the node from the front of the queue."""
        current = self.storage1.top

        while current:
            self.storage2.push(current.value)
            current = current.next
        self.storage2.pop()

        self.storage1 = Stack()

        current = self.storage2.top
        while current:
            self.storage1.push(current.value)
            current = current.next

        self.storage2 = Stack()


