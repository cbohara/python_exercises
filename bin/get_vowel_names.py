#!/usr/bin/env python3

def get_vowel_names(names):
	return [name
			for name in names
			if name[0].upper() in 'AEIOU']
