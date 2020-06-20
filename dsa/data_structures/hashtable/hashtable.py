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
            collection.append(current.data)
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
        hashed_key = self.hash(key)

        if not self.map[hashed_key]:
            self.map[hash_key] = LinkedList()

        self.map[hashed_key].add([key, value])

    def get(self):
        pass

    def contains(self):
        pass

    def hash(self, key):
        """
        1. split the key
        2. conver to ascii and add together
        3. multiple by prime
        4. % by self.size
        5. return
        """
        total = 0
        for char in key:
            total += ord(char)

        total += 19

        hashed_key = total % self.size

        return hashed_key
