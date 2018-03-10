#!/usr/bin/env python3
from numbers import Number

def deep_add(iterable_or_number, start=0):
	try:
		iter(iterable_or_number)
	except TypeError:
		return iterable_or_number
	else:
		return sum((deep_add(x) for x in iterable_or_number), start)
