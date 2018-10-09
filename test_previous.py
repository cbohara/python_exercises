import pytest
from previous import with_previous

def test_with_previous_with_string():
	actual = list(with_previous("hello"))
	expected = [('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')]
	assert actual == expected

def test_with_previous_with_list():
	actual = list(with_previous([1, 2, 3]))
	expected = [(1, None), (2, 1), (3, 2)]
	assert actual == expected
