#!/usr/bin/env python3
import string

def all_lower(input_str):
	return input_str.lower()

def remove_punctuation(input_str):
	translator = str.maketrans('', '', string.punctuation)
	return input_str.translate(translator)

def remove_whitespace(input_str):
	return "".join(input_str.split())

def clean(input_str):
	return remove_whitespace(remove_punctuation(all_lower(input_str)))

def is_anagram(string1, string2):
	return sorted(clean(string1)) == sorted(clean(string2))
