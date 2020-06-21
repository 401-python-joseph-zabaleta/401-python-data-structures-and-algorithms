class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        collection = []
        current = self.head
        while current:
            collection.append(current.data[0])
            current = current.next
        return collection

class Hashmap:
    """
    This class is used to implement a hashmap
    It has four available methods: Add, Get, Contains, Hash
    """
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def add(self, key, value):
        """Add is reponsible for adding data to the hashmap datas structure
        """
        hashed_key = self.hash(key)

        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()

        self.map[hashed_key].add([key, value])

    def get(self, key):
        """Get is responsible for taking in a key argument and returning the value for that key in the hashmap
        """
        index = self.hash(key)

        if self.map[index]:
            ll = self.map[index]

            while ll.head:
                if ll.head.data[0] == key:
                    return ll.head.data[1]
                else:
                    ll.head = ll.head.next
        else:
            return None

    def contains(self, key):
        """Contains is reponsible for returning a bool for wether or not the provided key is within the data structure
        """
        index = self.hash(key)

        if self.map[index]:
            collection = self.map[index].display()
            if key in collection:
                return True
            else:
                pass
        return False

    def hash(self, key):
        """
        Hash is responsible for splitting they key, converting to ascii values, adding them together, multiply it by any prime number, then modulous by the size of the hashmap to return a valid index value within the hashmap to store that key.
        """
        total = 0
        for char in key:
            total += ord(char)

        total *= 19

        hashed_key = total % self.size

        return hashed_key
