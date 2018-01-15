#!/usr/bin/env python3
import pytest
from lstrip import lstrip

def test_list():
	assert lstrip([0, 0, 1, 2, 3], 0) == [1, 2, 3]

def test_object_later_in_list():
	assert lstrip([0, 0, 1, 2, 0, 3], 0) == [1, 2, 0, 3]

def test_nothing_strip():
	assert lstrip([1, 2, 3], 0) == [1, 2, 3]

def test_string():
	assert lstrip('  hello', ' ') == ['h', 'e', 'l', 'l', 'o']

def test_string_with_space_later_in_string():
	assert lstrip('  hel lo', ' ') == ['h', 'e', 'l', ' ', 'l', 'o']

def test_empty_iterable():
	assert lstrip([], 1) == []

def test_strip_all():
	assert lstrip([1, 1, 1], 1) == []

def test_none_values():
	assert lstrip([None, 1, 2, 3], 0) == [None, 1, 2, 3]

def test_iterator():
	squares = (n**2 for n in [0, 0, 1, 2, 3])
	assert lstrip(squares, 0) == [1, 4, 9]
