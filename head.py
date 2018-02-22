#!/usr/bin/env python3
from itertools import islice

def head(iterable, n):
	if n < 0:
		n = 0
	return islice(iterable, n)
