def is_anagram(str1, str2):
	chars1 = [char for char in str1.lower() if char.isalpha()]
	chars2 = [char for char in str2.lower() if char.isalpha()]

	for char in chars1:
		if char in chars2:
			continue
		else:
			return False

	for char in chars2:
		if char in chars1:
			continue
		else:
			return False

	return True
