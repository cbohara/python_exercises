from decimal import Decimal
from datetime import timedelta
from fractions import Fraction
import pytest

from deep_add import deep_add


def test_shallow():
	assert deep_add([1, 2, 3, 4]) == 10

def test_with_empty_lists():
	assert deep_add([1, [2, 3, []], [], 4]) == 10
	assert deep_add([]) == 0

def test_deeply_nested_iterables():
	assert deep_add([[1, 2], [3, [4, [[[5]], 6]]]]) == 21

def test_non_numeric_types():
	with pytest.raises(TypeError):
		deep_add([1, [2, None]])

def test_other_numeric_types():
	assert deep_add([1.0, [3, 1.5]]) == 5.5
	assert deep_add([1.0, [3j]]) == 1+3j
	assert deep_add([Decimal('5.6'), 2]) == Decimal('7.6')
	assert deep_add([[Fraction(1)], Fraction(2)]) == Fraction(3)

def test_other_iterables():
	numbers = [1, 2, 3, 4]
	cubes_and_squares = ((n, (n**3, n**2)) for n in numbers)
	assert deep_add(cubes_and_squares) == 140
	assert deep_add([(1, 2), [3, {4, 5}]]) == 15

def test_start_value():
	numbers = [1, 2, 3, 4]
	assert deep_add(numbers, 0) == 10
	assert deep_add(numbers, 1) == 11
	assert deep_add(numbers, start=1) == 11
	assert deep_add([[], []], start=-10) == -10
