import pytest
from dsa.challenges.left_join.left_join import left_join

def test_example1():
    """Example from Instructions
    """
    hashmap1 = {
        'fond' : 'enamored',
        'wrath' : 'anger',
        'diligent' : 'employed',
        'outift' : 'garb',
        'guide' : 'usher',
    }

    hashmap2 = {
        'fond' : 'averse',
        'wrath' : 'delight',
        'diligent' : 'idle',
        'guide' : 'follow',
        'flow' : 'jam',
    }

    actual = left_join(hashmap1, hashmap2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
        ['diligent', 'employed', 'idle'],
        ['outift', 'garb', None],
        ['guide', 'usher', 'follow']
    ]
    assert actual == expected

def test_example2():
    """Flipped the inputed hashmaps from example
    """
    hashmap1 = {
        'fond' : 'enamored',
        'wrath' : 'anger',
        'diligent' : 'employed',
        'outift' : 'garb',
        'guide' : 'usher',
    }

    hashmap2 = {
        'fond' : 'averse',
        'wrath' : 'delight',
        'diligent' : 'idle',
        'guide' : 'follow',
        'flow' : 'jam',
    }

    actual = left_join(hashmap2, hashmap1)
    expected = [
        ['fond', 'averse', 'enamored'],
        ['wrath', 'delight', 'anger'],
        ['diligent', 'idle', 'employed'],
        ['guide', 'follow', 'usher'],
        ['flow', 'jam', None]
    ]
    assert actual == expected

def test_example3():
    """Different Variables and positions of them
    """
    hashmap1 = {
        'fond' : 'enamored',
        'food' : 'yummy',
        'diligent' : 'employed',
        'guide' : 'usher',
        'flow' : 'boom',
        'computer' : 'network',
    }

    hashmap2 = {
        'random': 'something',
        'fond' : 'averse',
        'wrath' : 'delight',
        'diligent' : 'idle',
        'guide' : 'follow',
        'flow' : 'jam',
    }

    actual = left_join(hashmap1, hashmap2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['food', 'yummy', None],
        ['diligent', 'employed', 'idle'],
        ['guide', 'usher', 'follow'],
        ['flow', 'boom', 'jam'],
        ['computer', 'network', None]
    ]

    assert actual == expected
