import pytest
from count import count_words


def test_simple_sentence():
	actual = count_words("oh what a day what a lovely day")
	expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
	assert actual == expected

def test_apostrophe():
	actual = count_words("don't stop believing")
	expected = {"don't": 1, 'stop': 1, 'believing': 1}
	assert actual == expected

def test_capitalization():
	actual = count_words("Oh what a day what a lovely day")
	expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
	assert actual == expected

#@pytest.mark.skip(reason='still working on bonus challenge')
def test_symbols():
	actual = count_words("¿Te gusta Python?")
	expected = {'te': 1, 'gusta': 1, 'python': 1}
	assert actual == expected

#@pytest.mark.skip(reason='still working on bonus challenge')
def test_punctuation_outside_words():
	actual = count_words("Oh what a day, what a lovely day!")
	expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
	assert actual == expected
