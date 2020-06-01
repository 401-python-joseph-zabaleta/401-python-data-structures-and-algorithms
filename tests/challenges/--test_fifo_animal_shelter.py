import pytest
from dsa.challenges.fifo_animal_shelter.fifo_animal_shelter import (
    Node,
    Dog,
    Cat,
    AnimalShelter,
    PseudoQueue
)

def test_AnimalShelter_enqueue_something():
    shelter = AnimalShelter()
    shelter.enqueue('something')
    actual = shelter.peek()
    expected = 'something'
    assert actual == expected

def test_AnimalShelter_enqueue_Dog():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    shelter.enqueue(oliver)
    actual = shelter.peek()
    expected = oliver
    assert actual == expected

def test_AnimalShelter_enqueue_Cat():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.peek()
    expected = cheeto
    assert actual == expected

def test_AnimalShelter_dequeue_no_pref():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.dequeue()
    expected = None
    assert actual == expected

def test_AnimalShelter_dequeue_pref_not_catOrDog():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.dequeue('bird')
    expected = None
    assert actual == expected

@pytest.mark.skip()
def test_AnimalShelter_dequeue_pref_dog():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.dequeue('dog')
    expected = 'cat'
    assert actual == expected

def test_PseudoQueue_enqueue_cat():
    shelter = PseudoQueue()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.storage1.peek().kind
    expected = 'cat'
    assert actual == expected
