import pytest
from dsa.challenges.repeated_word.repeated_word import word_most_often, repeated_word


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Once upon a time, there was a brave princess who...", "a"),
        ("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...", "it"),
        ("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...", "summer"),
    ],
)
def test_all(test_input, expected):
    actual = repeated_word(test_input)
    assert actual == expected

def test_random_string_one():
    string = 'Something that is random about this assignment is that this string is crazy!'
    actual = repeated_word(string)
    expected = 'is'
    assert actual == expected

def test_rnadom_string_two():
    string = "Random something going on here what is random about this"
    actual = repeated_word(string)
    expected = 'random'
    assert actual == expected
