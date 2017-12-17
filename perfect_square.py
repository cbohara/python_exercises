#!/usr/bin/env python3
from math import sqrt

def is_perfect_square(number):
	try:
		return sqrt(number).is_integer()
	except ValueError:
		return False
