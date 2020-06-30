import pytest
from dsa.data_structures.graph.graph import Graph

def test_node_graph():
    graph = Graph()
    node = graph.add_node('Test Node')
    actual = str(node)
    expected = 'Test Node'
    assert actual == expected

def test_node_graph_2():
    g = Graph()
    node1 = g.add_node('Test')
    node2 = g.add_node('random')
    actual = len(g.get_nodes())
    expected = 2
    assert actual == expected

def test_add_edge_exception_1():
    with pytest.raises(KeyError):
        g1 = Graph()
        g2 = Graph()
        node1 = g1.add_node(1)
        node2 = g2.add_node(2)
        g1.add_edge(node1, node2)

def test_add_edge_exception_2():
    with pytest.raises(KeyError):
        g1 = Graph()
        g2 = Graph()
        node1 = g1.add_node(1)
        node2 = g2.add_node(2)
        g2.add_edge(node1, node2)

def test_get_nodes():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    actual = len(graph.get_nodes())
    expected = 2
    assert actual == expected

def test_get_neighbors_none():
    g = Graph()
    node_a = g.add_node('a')
    node_b = g.add_node('b')
    node_c = g.add_node('c')
    node_d = g.add_node('d')
    actual = g.get_neighbors(node_a)
    expected = []
    assert actual == expected

def test_get_neighbors_1():
    g = Graph()
    node_a = g.add_node('a')
    node_b = g.add_node('b')
    node_c = g.add_node('c')
    node_d = g.add_node('d')
    g.add_edge(node_a, node_b)
    actual = len(g.get_neighbors(node_a))
    expected = 1
    assert actual == expected

def test_size_none():
    g = Graph()
    actual = g.size()
    expected = None
    assert actual == expected

def test_size_1():
    g = Graph()
    g.add_node(1)
    actual = g.size()
    expected = 1
    assert actual == expected

def test_size_2():
    g = Graph()
    g.add_node(235235)
    g.add_node(3232)
    g.add_node(222)
    actual = g.size()
    expected = 3
    assert actual == expected
