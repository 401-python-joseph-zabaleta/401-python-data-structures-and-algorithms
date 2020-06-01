class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)
        breadth = Queue()
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()

            if not front.left:
                front.left = new_node
            elif not front.right:
                front.right = new_node
            else:
                pass

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)



    def pre_order(self):
        """This is a Depth First traversal method. It prioritizes printing the `root` first, then looks to print `left` if left is not `None`, and lastly looks `right`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< root >>>
            collection.append(root.value)

            # <<< left
            walk(root.left)

            # right >>>
            walk(root.right)

        # end
        walk(self.root)

        return collection

    def in_order(self):
        """This is a Depth First traversal method. It prioritizes printing the `left` first, then prints the `root`, and lastly looks to print `right`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< left
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.left)

            # <<< root >>>
            collection.append(root.value)

            # right >>>
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.right)

        # Invoke
        walk(self.root)

        return collection

    def post_order(self):

        """This is a Depth First traversal method. It prioritizes print the `left` first, then looks to print the `right` and lastly prints the `root`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< left
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.left)


            # right >>>
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.right)

            # <<< root >>>
            collection.append(root.value)

        # Invoke
        walk(self.root)

        return collection

    def breadth_first(self):
        collection = []
        breadth = Queue()
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            collection.append(front.value)

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return collection

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """This will add a new element to the tree, based on a tradtional binary search tree condtional. If value is smaller than the root it will be added to the left, else add to the right."""

        node = Node(value)

        # Handles empty tree
        if not self.root:
            self.root = node
            return

        def walk(root, new_node):

            if not root:
                return

            # <<< left
            if new_node.value < root.value:

                if not root.left:
                    root.left = new_node
                else:
                    walk(root.left, new_node)

            # right >>>
            else:
                if not root.right:
                    root.right = new_node
                else:
                    walk(root.right, new_node)

        walk(self.root, node)

    def contains(self, value):
        """This searches the tree in order to verify that a given value exists in the tree. Returns a boolean value."""
        # Remember Pre_order returns a collection list
        if value in self.pre_order():
            return True
        else:
            return False

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
        return removed

    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        if not self.front:
            raise AttributeError("Can't peek from an empty queue")
        return self.front.value

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return not bool(self.front)


def fizz_buzz_tree(tree):
    pass
