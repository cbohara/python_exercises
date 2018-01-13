#!/usr/bin/env python3
import pytest
from lstrip import lstrip

def test_list():
	assert lstrip([0, 0, 1, 2, 3], 0) == [1, 2, 3]

def test_nothing_strip():
	assert lstrip([1, 2, 3], 0) == [1, 2, 3]

def test_string():
	assert lstrip('  hello', ' ') == 'hello'

def test_empty_iterable():
	assert lstrip([], 1) == []

def test_strip_all():
	assert lstrip([1, 1, 1], 1) == []

def test_none_values():
	assert lstrip([None, 1, 2, 3], 0) == [None, 1, 2, 3]

def test_iterator():
	squares = (n**2 for n in [0, 0, 1, 2, 3])
	assert lstrip(squares, 0) == [1, 4, 9]
