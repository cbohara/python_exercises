from parse_ranges import parse_ranges

def test_example_no_spaces():
	assert parse_ranges('1-2,4-4,8-10') == [1, 2, 4, 8, 9, 10]

def test_example_with_spaces():
	assert parse_ranges('0-0, 4-8, 20-20, 43-45') == [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
