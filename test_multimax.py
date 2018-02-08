#!/usr/bin/env python3
import pytest
from multimax import multimax

def test_single_max():
	assert multimax([1, 2, 4, 3]) == [4]

def test_two_max():
	assert multimax([1, 4, 2, 4, 3]) == [4, 4]

def test_all_max():
	assert multimax([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

def test_empty():
	assert multimax([]) == []

def test_iterator():
	numbers = [1, 4, 2, 4, 3]
	squares = (n**2 for n in numbers)
	assert multimax(squares) == [16, 16]

@pytest.mark.bonus1
def test_key_function():
	words = ["alligator", "animal", "apple", "artichoke", "avalanche"]
	outputs = ["alligator", "artichoke", "avalanche"]
	assert multimax(words, key=len) == outputs

@pytest.mark.bonus2
def test_lists():
	inputs = [[0], [1], [], [0, 1], [1]]
	expected = [[1], [1]]
	assert multimax(inputs) == expected

@pytest.mark.bonus3
def test_order_maintained():
	inputs = [
		(3, 2),
		(2, 1),
		(3, 2),
		(2, 0),
		(3, 2),
	]
	expected = [
		inputs[0],
		inputs[2],
		inputs[4],
	]
	outputs = multimax(inputs)
	assert outputs == expected
