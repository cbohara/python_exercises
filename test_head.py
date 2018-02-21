#!/usr/bin/env python3
import pytest
from head import head

def test_zero():
	assert head([1, 2], 0) == []

def test_one():
	assert head([1, 2], 1) == [1]

def test_two():
	assert head([1, 2], 2) == [1, 2]

def test_iterator():
	nums = (n**2 for n in [1, 2, 3, 4])
	assert head(nums, 2) == [1, 4]

def test_n_larger_than_iterable_length():
	nums = (n**2 for n in [1, 2, 3, 4])
	assert head(nums, 5) == [1, 4, 9, 16]
	assert head((), 10) == []

def test_negative_n():
	nums = (n**2 for n in [1, 2, 3, 4])
	assert head(nums, -1) == []
	assert head((), -9) == []

@pytest.mark.skip(reason='not sure if I want to convert all to iterator')
def test_returns_iterator():
	nums = (n**2 for n in [1, 2, 3, 4])
	output = iter(head(nums, 2))
	assert next(output) == 1
	assert next(output) == 2
