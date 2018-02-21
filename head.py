#!/usr/bin/env python3

def head(iterator, n):
	input_list = list(iterator)
	if n <= 0:
		return []
	elif n > len(input_list):
		return input_list
	else:
		return input_list[:n]
