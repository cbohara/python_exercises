#!/usr/bin/env python3
import pytest
from head import head

def iterator_to_list(iterator):
	return list(iterator)

def test_zero():
	assert iterator_to_list(head([1, 2], 0)) == []

def test_one():
	assert iterator_to_list(head([1, 2], 1)) == [1]

def test_two():
	assert iterator_to_list(head([1, 2], 2)) == [1, 2]

def test_iterator():
	nums = (n**2 for n in [1, 2, 3, 4])
	assert iterator_to_list(head(nums, 2)) == [1, 4]

def test_n_larger_than_iterable_length():
	nums = (n**2 for n in [1, 2, 3, 4])
	assert iterator_to_list(head(nums, 5)) == [1, 4, 9, 16]
	assert iterator_to_list(head((), 10)) == []

def test_negative_n():
	nums = (n**2 for n in [1, 2, 3, 4])
	assert iterator_to_list(head(nums, -1)) == []
	assert iterator_to_list(head((), -9)) == []

def test_returns_iterator():
	nums = (n**2 for n in [1, 2, 3, 4])
	output = head(nums, 2)
	assert next(output) == 1
