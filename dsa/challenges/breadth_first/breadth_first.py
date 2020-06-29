from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        """Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance."""
        self.storage.appendleft(value)

    def dequeue(self):
        """Takes no arguments, remove the node from the front of the queue, and returns the node's value."""
        return self.storage.pop()

    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        return self.storage[-1]

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return len(self.storage) == 0


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        """ Takes in a value to create a new node/vertex for the graph. Returns the added node.
        """
        node = Vertex(value)
        self.graph[node] = []
        return node

    def add_edge(self, vertex1, vertex2, weight=1):
        """ Takes in two nodes to be linked together with an edge. Third parameter is the ability to add a weight to the edge.
        """
        if vertex1 not in self.graph:
            raise KeyError('Vertex1 is not in the graph')

        if vertex2 not in self.graph:
            raise KeyError('Vertex2 is not in the graph')


        edge = Edge(vertex2, weight)
        self.graph[vertex1].append(edge)

    def get_nodes(self):
        """ Returns all vertices/nodes within the graph as a collection
        """
        return self.graph.keys()

    def get_neighbors(self, vertex):
        """ Takes in a vertex/node and returns a collection of edges connected to the given vertex/node as well as the weight of the connection.
        """
        collection = []
        connections =  self.graph.get(vertex, [])

        for neighbor in connections:
            holder = {}
            holder[neighbor] = neighbor.weight
            collection.append(holder)

        return collection

    def size(self):
        """ Returns the total number of vertices/nodes in the graph
        """
        return len(self.graph) if len(self.graph) > 0 else None

    def breadth_first(self, vertex):
        """ Takes in a node/vertex and performs a breadth first traversal of the graph. This will return a collection of the nodes/vertices within the graph from a breadth first traversal perspective of the given node/vertex.
        """
        nodes = []
        holder = set()
        breadth = Queue()
        holder.add(vertex.value)
        breadth.enqueue(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self.graph[front]:
                if child.vertex.value not in holder:
                    holder.add(child.vertex.value)
                    breadth.enqueue(child.vertex)

        return nodes
