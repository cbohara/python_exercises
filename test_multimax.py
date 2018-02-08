#!/usr/bin/env python3
from multimax import multimax

def test_single_max():
	assert multimax([1, 2, 4, 3]) == [4]

def test_two_max():
	assert multimax([1, 4, 2, 4, 3]) == [4, 4]

def test_all_max():
	assert multimax([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

def test_empty():
	assert multimax([]) == []
