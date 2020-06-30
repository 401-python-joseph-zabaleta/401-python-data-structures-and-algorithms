import pytest
from dsa.challenges.breadth_first.breadth_first import Graph

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

def test_breadth_first_example():
    """ Refer to the README Examples for visual aids.
    """
    g = Graph()
    pandora = g.add_node('Pandora')
    adrendelle = g.add_node('Arendelle')
    metroville = g.add_node('Metroville')
    monstroplolis = g.add_node('Monstroplolis')
    naboo = g.add_node('Naboo')
    narnia = g.add_node('Narnia')
    g.add_edge(pandora, adrendelle)
    g.add_edge(adrendelle, metroville)
    g.add_edge(adrendelle, monstroplolis)
    g.add_edge(adrendelle, pandora)
    g.add_edge(metroville, adrendelle)
    g.add_edge(metroville, monstroplolis)
    g.add_edge(metroville, narnia)
    g.add_edge(metroville, naboo)
    g.add_edge(monstroplolis, adrendelle)
    g.add_edge(monstroplolis, metroville)
    g.add_edge(monstroplolis, naboo)
    g.add_edge(naboo, narnia)
    g.add_edge(naboo, metroville)
    g.add_edge(naboo, monstroplolis)
    actual = g.breadth_first(pandora)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    assert actual == expected

def test_breadth_first_example_2():
    """ Refer to the README Examples for visual aids.
    """
    g = Graph()
    bob = g.add_node('Bob')
    tom = g.add_node('Tom')
    sam = g.add_node('Sam')
    joe = g.add_node('Joe')
    jon = g.add_node('Jon')
    g.add_edge(bob, tom)
    g.add_edge(tom, bob)
    g.add_edge(tom, jon)
    g.add_edge(tom, sam)
    g.add_edge(tom, joe)
    g.add_edge(jon, tom)
    g.add_edge(jon, sam)
    g.add_edge(sam, jon)
    g.add_edge(sam, tom)
    g.add_edge(sam, joe)
    g.add_edge(joe, sam)
    g.add_edge(joe, tom)
    actual = g.breadth_first(bob)
    expected = ['Bob', 'Tom', 'Jon', 'Sam', 'Joe']
    assert actual == expected

def test_breadth_first_example_2_different_start():
    g = Graph()
    bob = g.add_node('Bob')
    tom = g.add_node('Tom')
    sam = g.add_node('Sam')
    joe = g.add_node('Joe')
    jon = g.add_node('Jon')
    g.add_edge(bob, tom)
    g.add_edge(tom, bob)
    g.add_edge(tom, jon)
    g.add_edge(tom, sam)
    g.add_edge(tom, joe)
    g.add_edge(jon, tom)
    g.add_edge(jon, sam)
    g.add_edge(sam, jon)
    g.add_edge(sam, tom)
    g.add_edge(sam, joe)
    g.add_edge(joe, sam)
    g.add_edge(joe, tom)
    actual = g.breadth_first(tom)
    expected = ['Tom', 'Bob', 'Jon', 'Sam', 'Joe']
    assert actual == expected
