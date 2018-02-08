#!/usr/bin/env python3

def multimax(iterable):
	input_list = list(iterable)
	if len(input_list) > 0:
		max_value = max(input_list)
		return [x for x in input_list if max_value == x]
	else:
		return []
