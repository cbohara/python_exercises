import re
from collections import Counter


def ignore_punctuation_outside(word):
	"""
	Ignore punctuation outside word
	Keep punctuation inside word

	Args:
		word (str)
	Returns:
		string
	"""
	first_char = word[0]
	last_char = word[-1]
	if not first_char.isalpha() and not last_char.isalpha():
		return word[1:-1]
	elif not first_char.isalpha() and last_char.isalpha():
		return word[1:]
	elif first_char.isalpha() and not last_char.isalpha():
		return word[:-1]
	else:
		return word


def count_words(input_str):
	"""
	Return mapping with words as the keys and the number of times each word was seen as the values
	Ignore punctuation outside of words

	Args:
		input_str (str) can contain upper/lower case char, various punctuation

	Returns:
		dictionary representing word counts
	"""
	return Counter(re.findall(r"\b[\w'-]+\b", input_str.lower()))
