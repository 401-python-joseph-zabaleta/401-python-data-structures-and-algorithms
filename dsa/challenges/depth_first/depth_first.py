class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Stack:
    def __init__(self, item=None):
        self.top = item

    def push(self, item):
        if self.top == None:
            self.top = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            raise AttributeError("Can't pop item for an empty stack")
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.value

    def peek(self):
        if not self.top:
            raise AttributeError("Can't peek top from an empty stack")
        return self.top.value

    def is_empty(self):
        return not bool(self.top)

def depth_first(graph, root):
    """ This is a depth first traversal for a graph, this is a standalone function, that takes in two arguments: adjanceny list graph, and any root with to start from in that graph.
    """
    storage = Stack()
    visited = []

    storage.push(root)
    visited.append(root.value)

    while not storage.is_empty():

        top = storage.peek()
        status = False

        for child in graph.graph[top]:

            if child.vertex.value not in visited:
                status = True
                storage.push(child.vertex)
                visited.append(child.vertex.value)
                break

        if status:
            continue
        else:
            storage.pop()

    return visited




