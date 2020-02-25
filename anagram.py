def normalized_set(string):
	return {char for char in string.lower() if char.isalpha()}


def is_anagram(str1, str2):
	chars1 = normalized_set(str1)
	chars2 = normalized_set(str2)

	if len(chars1) != len(chars2):
		return False

	if len(chars1.difference(chars2)) == 0:
		return True
	else:
		return False
