from compact import compact


def test_compact_empty_list():
	assert compact([]) == []


def test_compact_all_same_value():
	assert compact([1, 1, 1]) == [1]


def test_compact_assorted_values():
	assert compact([1, 1, 2, 2, 3, 2]) == [1, 2, 3, 2]


def test_compact_tuple():
	tup = (1, 1, 2, 2, 3, 2)
	assert compact(tup) == [1, 2, 3, 2]


def test_iterable_argument():
	assert compact(n**2 for n in [1, 2, 2]) == [1, 4]
