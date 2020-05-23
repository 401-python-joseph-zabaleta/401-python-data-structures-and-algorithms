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
    def __init__(self):
        self.storage = []

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        try:
            return self.storage.pop()
        except IndexError:
            return "Can't pop item from an empty stack"

    def peek(self):
        try:
            return self.storage[-1]
        except IndexError:
            return "Can't peek top from an empty stack"

    def is_empty(self):
        return not bool(len(self.storage))


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, item):
        pass

    def dequeue(self, item):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass



# class Queue:
#     def __init__(self):
#         self.storage = deque()

#     def enqueue(self, item):
#         self.storage.appendleft(item) #O(1)

#     def dequeue(self):
#         return self.storage.pop()

#     def peek(self):
#         return self.storage[-1]

#     def is_empty(self):
#         return not len(self.storage)
