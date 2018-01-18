from operator import itemgetter

from group_by import group_by

def check_even(num):
	if num % 2 == 0:
		return 'Even'
	else:
		return 'Odd'

def test_list_of_ints():
	my_nums = [1, 4, 5, 6, 8, 19, 34, 55]
	expected = {
		'Odd': [1, 5, 19, 55],
		'Even': [4, 6, 8, 34]
	}
	output = group_by(my_nums, key_func=check_even)
	assert output == expected

def test_tuples_of_strings():
	animals = [
		('agatha', 'dog'),
		('kurt', 'cat'),
		('margaret', 'mouse'),
		('cory', 'cat'),
		('mary', 'mouse'),
	]
	expected = {
		'mouse': [('margaret', 'mouse'), ('mary', 'mouse')],
		'dog': [('agatha', 'dog')],
		'cat': [('kurt', 'cat'), ('cory', 'cat')],
	}
	output = group_by(animals, key_func=itemgetter(1))
	assert output == expected

def test_strings():
	words = ['Apple', 'animal', 'apple', 'ANIMAL', 'animal']
	expected = {
		'apple': ['Apple', 'apple'],
		'animal': ['animal', 'ANIMAL', 'animal'],
	}
	output = group_by(words, key_func=str.lower)
	assert output == expected

def test_default_bonus():
	nums = [1, 2, 1, 3, 2, 1]
	expected = {1: [1, 1, 1], 2: [2, 2], 3: [3]}
	output = group_by(nums)
	assert output == expected
