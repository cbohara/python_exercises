from compact import compact


def test_compact_all_same_value():
	assert compact([1, 1, 1]) == [1]


def test_compact_assorted_values():
	assert compact([1, 1, 2, 2, 3, 2]) == [1, 2, 3, 2]


def test_compact_empty_list():
	assert compact([]) == []
