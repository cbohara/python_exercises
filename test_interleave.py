#!/usr/bin/env python3
import pytest
from interleave import interleave

@pytest.mark.simple
def test_empty_lists():
	assert interleave([], []) == []

@pytest.mark.simple
def test_single_item_lists():
	assert interleave([1], [2]) == [1, 2]

@pytest.mark.simple
def test_two_item_lists():
	assert interleave([1, 2], [3, 4]) == [1, 3, 2, 4]

@pytest.mark.simple
def test_two_lists():
	list1 = [1, 2, 3, 4]
	list2 = [5, 6, 7, 8]
	assert interleave(list1, list2) == [1, 5, 2, 6, 3, 7, 4, 8]

@pytest.mark.simple
def test_none_value():
	list1 = [1, 2, 3, None]
	list2 = [4, 5, 6, 7]
	assert interleave(list1, list2) == [1, 4, 2, 5, 3, 6, None, 7]

@pytest.mark.generator
def test_list_and_generator_comprehension():
	nums = [1, 2, 3, 4]
	squares = (n**2 for n in nums)
	assert interleave(nums, squares) == [1, 1, 2, 4, 3, 9, 4, 16]

@pytest.mark.multiple
def test_three_arguments():
	list1 = [1, 2, 3]
	list2 = [4, 5, 6]
	list3 = [7, 8, 9]
	assert interleave(list1, list2, list3) == [1, 4, 7, 2, 5, 8, 3, 6, 9]

@pytest.mark.alt_lengths
def test_two_arguments_alternative_lengths():
	list1 =[1, 2, 3]
	list2 = [4, 5, 6, 7, 8]
	assert interleave(list1, list2) == [1, 4, 2, 5, 3, 6, 7, 8]
