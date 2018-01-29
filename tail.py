#!/usr/bin/env python3

def tail(iterable, n):
	if n <= 0:
		return []
	return list(iterable)[-n:]
