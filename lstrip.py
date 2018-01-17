#!/usr/bin/env python3
from itertools import dropwhile

def lstrip(iterable, strip_value):
	def is_stripped_value(value): return value == strip_value
	return dropwhile(is_stripped_value, iterable)
