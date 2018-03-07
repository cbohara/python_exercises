#!/usr/bin/env python3

def deep_add(list_or_number):
	total = 0
	if type(list_or_number) == list:
		for x in list_or_number:
			total += deep_add(x)
		return total
	else:
		return list_or_number
