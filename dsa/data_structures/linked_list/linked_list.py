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
        """Function creates a new node and adds it to the linked list"""
        self.head = Node(value, self.head)

    def includes(self, value):
        """Returns whether or not a value is within the linked list. Boolean output"""
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"
