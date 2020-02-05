import re


def ignore_punctuation_outside(word):
	"""
	Ignore punctuation outside word
	Keep punctuation inside word

	Args:
		word (str)
	Returns:
		string
	"""
	pass


def count_words(input_str):
	"""
	Return mapping with words as the keys and the number of times each word was seen as the values
	Ignore punctuation outside of words

	Args:
		input_str (str) can contain upper/lower case char, various punctuation

	Returns:
		dictionary representing word counts
	"""
	mapping = {}
	words = input_str.lower().split()
	for word in words:
		if word not in mapping:
			mapping[word] = 1
		elif word in mapping:
			mapping[word] += 1
	return mapping
