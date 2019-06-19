import pytest
from compact import compact


def test_compact_empty_list():
	c = compact([])
	with pytest.raises(StopIteration):
		next(c)


def test_compact_list_all_same_value():
	c = compact([1, 1, 1])
	assert iter(c) is c
	assert next(c) == 1
	with pytest.raises(StopIteration):
		next(c)


def test_compact_list_assorted_values():
	c = compact([1, 1, 2, 2, 3, 2])
	assert iter(c) is c
	assert next(c) == 1
	assert next(c) == 2
	assert next(c) == 3
	assert next(c) == 2
	with pytest.raises(StopIteration):
		next(c)


def test_compact_tuple_assorted_values():
	tup = (1, 1, 2, 2, 3, 2)
	c = compact(tup)
	assert iter(c) is c
	assert next(c) == 1
	assert next(c) == 2
	assert next(c) == 3
	assert next(c) == 2
	with pytest.raises(StopIteration):
		next(c)


def test_compact_iterable():
	c = compact(n**2 for n in [1, 2, 2])
	assert iter(c) is c
	assert next(c) == 1
	assert next(c) == 4
	with pytest.raises(StopIteration):
		next(c)


def test_compact_return_iterable():
	c = compact(n**2 for n in [1, 2, 2])
	assert iter(c) is c
	assert next(c) == 1
	assert next(c) == 4
	with pytest.raises(StopIteration):
		next(c)
