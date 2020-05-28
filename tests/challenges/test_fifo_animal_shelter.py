import pytest
from dsa.challenges.fifo_animal_shelter.fifo_animal_shelter import (
    Node,
    Stack,
    AnimalShelter
)

def test_AnimalShelter_enqueue():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    actual = str(shelter.inbox)
    expected = 'something'
    assert actual == expected
