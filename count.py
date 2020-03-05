import re
from collections import Counter


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
