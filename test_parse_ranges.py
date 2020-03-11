import pytest
from parse_ranges import parse_ranges

def test_example_no_spaces():
	numbers = parse_ranges('1-2,4-4,8-10')
	assert list(numbers) == [1, 2, 4, 8, 9, 10]

def test_example_with_spaces():
	numbers = parse_ranges('0-0, 4-8, 20-20, 43-45')
	assert list(numbers) == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]

def test_bonus_return_generator():
	numbers = parse_ranges('100-10000')
	assert next(numbers) == 100
	assert next(numbers) == 101
