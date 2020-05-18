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
                return "Value not found."
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


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"
