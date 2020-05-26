class LinkedList:
    def __init__(self, value=None):
        self.head = None

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += f"{{ {str(current.value)} }} -> "
            current = current.next
        return output + "NULL"

    def __repr__(self):
        return f"LinkedList: {self.head}"

    def insert(self, value):
        """Function creates a new node and adds it to the head of the linked list"""
        self.head = Node(value, self.head)

    def insertBefore(self, value, newVal):
        """Function has two parameters a value: inside the linked list and newVal: item to be added. This will create a new node with the newVal and insert it before the given value"""
        current = self.head

        while current:
            if current.next == None:
                return "Value not found."
            if current.next.value == value:
                current.next = Node(newVal, current.next)
                break
            current = current.next

    def insertAfter(self, value, newVal):
        """Function has two parameters a value: inside the linked list and newVal: item to be added. This will create a new node with the newVal and insert it after the given value"""
        current = self.head

        while current:
            if current.next == None:
                raise ValueError("Value not found.")
            if current.value == value:
                current.next = Node(newVal, current.next)
                break
            current = current.next

    def includes(self, value):
        """Returns whether or not a value is within the linked list. Boolean output"""
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        """Function creates a new node and appends it to the tail of the linked list"""
        current = self.head

        while current:
            if current.next == None:
                current.next = Node(value)
                break
            current = current.next

    def kth_from_end(self, k):
        """Returns the value of a node that is k value from the end. Parameter k is an positive integer"""
        if k < 0:
            raise ValueError("Positive integer required")

        current = self.head
        arr = []
        while current:
            arr.append(current)
            current = current.next

        if len(arr) < k:
            raise IndexError("Value extends length of List.")

        arr.reverse()

        if k == len(arr):
            k = k - 1
        return arr[k].value


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
        if not self.top:
            raise AttributeError("Can't pop item from an empty stack")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value
        # try:
        #     popped_node = self.top
        #     self.top = self.top.next
        #     popped_node.next = None
        #     return popped_node.value
        # except AttributeError:
        #     return "Can't pop item from an empty stack"

    def peek(self):
        """Takes no arguments and returns the value of the node located on top of the stack, without removing it from the stack."""
        if not self.top:
            raise AttributeError("Can't peek top from an empty stack")
        return self.top.value
        # try:
        #     return self.top.value
        # except AttributeError:
        #     return "Can't peek top from an empty stack"

    def is_empty(self):
        """Takes no arguments, and returns a boolean indicating whether or not the stack is empty."""
        return not bool(self.top)


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

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
        if not self.front:
            raise AttributeError("Can't dequeue from an empty queue")

        removed = self.front
        self.front = self.front.next
        return removed.value
        # try:
        #     removed = self.front
        #     self.front = self.front.next
        #     return removed.value
        # except AttributeError:
        #     return "Can't dequeue from an empty queue"

    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        if not self.front:
            raise AttributeError("Can't peek from an empty queue")
        return self.front.value

        # try:
        #     return self.front.value
        # except AttributeError:
        #     return "Can't peek front from an empty queue"

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return not bool(self.front)
