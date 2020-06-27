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
