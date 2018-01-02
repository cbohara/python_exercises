#!/usr/bin/env python3

def only_alpha_char(string):
	return sorted(
		char
		for char in string.lower()
		if char.isalpha()
	)

def is_anagram(string1, string2):
	return only_alpha_char(string1) == only_alpha_char(string2)
