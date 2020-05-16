class LinkedList:
    def __init__(self, value=None):
        self.head = None

    def __str__(self):

        res = ""

        current = self.head

        while current:
            res += "{ " + str(current.value) + " } -> "
            current = current.next
        return res + "NULL"

    def __repr__(self):
        return f"LinkedList: {self.head}"

    def insert(self, value):
        self.head = Node(value, self.head)


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"
