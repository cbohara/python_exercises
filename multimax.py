#!/usr/bin/env python3

def multimax(iterable, key=None):
	maxs = []
	for item in iterable:
		if not maxs or maxs[0] == item:
			maxs.append(item)
		elif item > maxs[0]:
			maxs = [item]
	return maxs
