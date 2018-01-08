#!/usr/bin/env python3
import pytest
from interleave import interleave

def test_two_lists():
	list1 = [1, 2, 3, 4]
	list2 = [5, 6, 7, 8]
	assert interleave(list1, list2) == [1, 5, 2, 6, 3, 7, 4, 8]

def test_list_and_generator_comprehension():
	nums = [1, 2, 3, 4]
	squares = (n**2 for n in nums)
	assert interleave(nums, squares) == [1, 1, 2, 4, 3, 9, 4, 16]
