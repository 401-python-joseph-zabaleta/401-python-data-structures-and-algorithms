import pytest
from dsa.challenges.breadth_first.breadth_first import Graph
from dsa.challenges.get_edges.get_edges import get_edges

def test_example_input_1():
    g = Graph()
    pandora = g.add_node('Pandora')
    adrendelle = g.add_node('Arendelle')
    metroville = g.add_node('Metroville')
    monstroplolis = g.add_node('Monstroplolis')
    naboo = g.add_node('Naboo')
    narnia = g.add_node('Narnia')
    g.add_edge(pandora, adrendelle, 150)
    g.add_edge(pandora, metroville, 82)
    g.add_edge(adrendelle, pandora, 150)
    g.add_edge(adrendelle, metroville, 99)
    g.add_edge(adrendelle, monstroplolis, 42)
    g.add_edge(metroville, pandora, 82)
    g.add_edge(metroville, adrendelle, 99)
    g.add_edge(metroville, monstroplolis, 105)
    g.add_edge(metroville, naboo, 26)
    g.add_edge(metroville, narnia, 37)
    g.add_edge(monstroplolis, metroville, 73)
    g.add_edge(monstroplolis, adrendelle, 42)
    g.add_edge(monstroplolis, naboo, 73)
    g.add_edge(naboo, monstroplolis, 73)
    g.add_edge(naboo, metroville, 26)
    g.add_edge(naboo, narnia, 250)
    g.add_edge(narnia, naboo, 250)
    g.add_edge(narnia, metroville, 37)
    actual = get_edges(g, [metroville, pandora])
    expected = (True, '$82',)
    assert actual == expected

def test_example_input_2():
    g = Graph()
    pandora = g.add_node('Pandora')
    adrendelle = g.add_node('Arendelle')
    metroville = g.add_node('Metroville')
    monstroplolis = g.add_node('Monstroplolis')
    naboo = g.add_node('Naboo')
    narnia = g.add_node('Narnia')
    g.add_edge(pandora, adrendelle, 150)
    g.add_edge(pandora, metroville, 82)
    g.add_edge(adrendelle, pandora, 150)
    g.add_edge(adrendelle, metroville, 99)
    g.add_edge(adrendelle, monstroplolis, 42)
    g.add_edge(metroville, pandora, 82)
    g.add_edge(metroville, adrendelle, 99)
    g.add_edge(metroville, monstroplolis, 105)
    g.add_edge(metroville, naboo, 26)
    g.add_edge(metroville, narnia, 37)
    g.add_edge(monstroplolis, metroville, 73)
    g.add_edge(monstroplolis, adrendelle, 42)
    g.add_edge(monstroplolis, naboo, 73)
    g.add_edge(naboo, monstroplolis, 73)
    g.add_edge(naboo, metroville, 26)
    g.add_edge(naboo, narnia, 250)
    g.add_edge(narnia, naboo, 250)
    g.add_edge(narnia, metroville, 37)
    actual = get_edges(g, [adrendelle, monstroplolis, naboo])
    expected = (True, '$115',)
    assert actual == expected

def test_example_input_3():
    g = Graph()
    pandora = g.add_node('Pandora')
    adrendelle = g.add_node('Arendelle')
    metroville = g.add_node('Metroville')
    monstroplolis = g.add_node('Monstroplolis')
    naboo = g.add_node('Naboo')
    narnia = g.add_node('Narnia')
    g.add_edge(pandora, adrendelle, 150)
    g.add_edge(pandora, metroville, 82)
    g.add_edge(adrendelle, pandora, 150)
    g.add_edge(adrendelle, metroville, 99)
    g.add_edge(adrendelle, monstroplolis, 42)
    g.add_edge(metroville, pandora, 82)
    g.add_edge(metroville, adrendelle, 99)
    g.add_edge(metroville, monstroplolis, 105)
    g.add_edge(metroville, naboo, 26)
    g.add_edge(metroville, narnia, 37)
    g.add_edge(monstroplolis, metroville, 73)
    g.add_edge(monstroplolis, adrendelle, 42)
    g.add_edge(monstroplolis, naboo, 73)
    g.add_edge(naboo, monstroplolis, 73)
    g.add_edge(naboo, metroville, 26)
    g.add_edge(naboo, narnia, 250)
    g.add_edge(narnia, naboo, 250)
    g.add_edge(narnia, metroville, 37)
    actual = get_edges(g, [naboo, pandora])
    expected = (False, '$0')
    assert actual == expected

def test_example_input_4():
    g = Graph()
    pandora = g.add_node('Pandora')
    adrendelle = g.add_node('Arendelle')
    metroville = g.add_node('Metroville')
    monstroplolis = g.add_node('Monstroplolis')
    naboo = g.add_node('Naboo')
    narnia = g.add_node('Narnia')
    g.add_edge(pandora, adrendelle, 150)
    g.add_edge(pandora, metroville, 82)
    g.add_edge(adrendelle, pandora, 150)
    g.add_edge(adrendelle, metroville, 99)
    g.add_edge(adrendelle, monstroplolis, 42)
    g.add_edge(metroville, pandora, 82)
    g.add_edge(metroville, adrendelle, 99)
    g.add_edge(metroville, monstroplolis, 105)
    g.add_edge(metroville, naboo, 26)
    g.add_edge(metroville, narnia, 37)
    g.add_edge(monstroplolis, metroville, 73)
    g.add_edge(monstroplolis, adrendelle, 42)
    g.add_edge(monstroplolis, naboo, 73)
    g.add_edge(naboo, monstroplolis, 73)
    g.add_edge(naboo, metroville, 26)
    g.add_edge(naboo, narnia, 250)
    g.add_edge(narnia, naboo, 250)
    g.add_edge(narnia, metroville, 37)
    actual = get_edges(g, [narnia, adrendelle, naboo])
    expected = (False, '$0')
    assert actual == expected

def test_example_input_around_the_world():
    g = Graph()
    pandora = g.add_node('Pandora')
    adrendelle = g.add_node('Arendelle')
    metroville = g.add_node('Metroville')
    monstroplolis = g.add_node('Monstroplolis')
    naboo = g.add_node('Naboo')
    narnia = g.add_node('Narnia')
    g.add_edge(pandora, adrendelle, 150)
    g.add_edge(pandora, metroville, 82)
    g.add_edge(adrendelle, pandora, 150)
    g.add_edge(adrendelle, metroville, 99)
    g.add_edge(adrendelle, monstroplolis, 42)
    g.add_edge(metroville, pandora, 82)
    g.add_edge(metroville, adrendelle, 99)
    g.add_edge(metroville, monstroplolis, 105)
    g.add_edge(metroville, naboo, 26)
    g.add_edge(metroville, narnia, 37)
    g.add_edge(monstroplolis, metroville, 73)
    g.add_edge(monstroplolis, adrendelle, 42)
    g.add_edge(monstroplolis, naboo, 73)
    g.add_edge(naboo, monstroplolis, 73)
    g.add_edge(naboo, metroville, 26)
    g.add_edge(naboo, narnia, 250)
    g.add_edge(narnia, naboo, 250)
    g.add_edge(narnia, metroville, 37)
    actual = get_edges(g, [pandora, metroville, narnia, naboo, monstroplolis, adrendelle, pandora])
    expected = (True, '$634')
    assert actual == expected