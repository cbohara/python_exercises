#!/usr/bin/env python3
import pytest
from with_previous import with_previous

def test_three():
	inputs = [1, 2, 3]
	outputs = [(1, None), (2, 1), (3,2)]
	assert with_previous(inputs) == outputs

def test_empty():
	inputs = []
	outputs = []
	assert with_previous(inputs) == outputs

def test_one_item():
	inputs = [1]
	outputs = [(1, None)]
	assert with_previous(inputs) == outputs

def test_none():
	inputs = [None, None, None]
	outputs = [(None, None), (None, None), (None, None)]
	assert with_previous(inputs) == outputs

def test_string():
	inputs = 'hey'
	outputs = [('h', None), ('e', 'h'), ('y', 'e')]
	assert with_previous(inputs) == outputs

def test_lazy_iterable():
	inputs = (n*n for n in [1, 2, 3])
	outputs = [(1, None), (4, 1), (9, 4)]
	assert with_previous(inputs) == outputs
