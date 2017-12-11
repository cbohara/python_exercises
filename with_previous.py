#!/usr/bin/env python3

def with_previous(iterable):
	output = []
	prev_value = None
	for value in iterable:
		output.append((value, prev_value))
		prev_value = value
	return output
