# Graph
[Table of Contents](../../../README.md)
## Challenge 30
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

1. `add_node()`
- [x] Adds a new node to the graph
- [x] Takes in the value of that node
- [x] Returns the added node
2. `add_edge()`
- [x] Adds a new edge between two nodes in the graph
- [x] Include the ability to have a “weight”
- [x] Takes in the two nodes to be connected by the edge
    - [x] Both nodes should already be in the Graph
3. `get_nodes()`
- [x] Returns all of the nodes in the graph as a collection (set, list, or similar)
4. `get_neighbors()`
- [x] Returns a collection of edges connected to the given node
- [x] Takes in a given node
- [x] Include the weight of the connection in the returned collection
5. `size()`
- [x] Returns the total number of nodes in the graph

## User Tests
- [x] Node can be successfully added to the graph
- [x] An edge can be successfully added to the graph
- [x] A collection of all nodes can be properly retrieved from the graph
- [x] All appropriate neighbors can be retrieved from the graph
- [x] Neighbors are returned with the weight between nodes included
- [x] The proper size is returned, representing the number of nodes in the graph
- [x] A graph with only one node and edge can be properly returned
- [x] An empty graph properly returns null

## Approach & Efficiency
Graph is using a hashmap to stores in data. It has 5 methods which are add_node(), add_edge(), get_nodes(), get_neighbors(), size(). All operations are O(1) time complexity except for get_neightbors(). Getting the neighsbors has a for loop inside of it that is looping over the list of edges that a particular node has, and gathering the weight values for the output.

## API
1. `add_node()`:
    - Takes in a value, creates a node, then adds this node to our graph. O(1) time as we are working with a dictionary and assign just variable names. Returns the node at the end.
2. `add_edge()`:
    - Takes in two nodes, creates an edge from first node to the second node. Looks up first node, then adds the edge to the list of neighbors. O(1) operations.
3. `get_nodes()`:
    - Takes no arguments, and returns a list of all the keys in the dictionary. This function is a O(1) operation as it will retrieve the key list from the dictionary.
4. `get_neighbors()`:
    - Takes in a node, will retreive the edge list from graph. It will loop over the list to access each edge, creating a key:value pair of the edge along with the weight it has, then appending it to a collection list. At the end returns the collection. This is an O(N) operation based on the number of edges a node has, as well as O(1) space for the collection.
5. `size()`:
    - Returns the size of the graph, this is an O(1) operation as its a retrieval of the size attribute.
