#!/usr/bin/env python3

def multimax(iterable, key=None):
	if key is None:
		def key(item): return item
	max_key = None
	maxs = []
	for item in iterable:
		print("item", item)
		k = key(item)
		print("k", k)
		if k == max_key:
			maxs.append(item)
		elif not maxs or k > max_key:
			maxs = [item]
			max_key = k
	return maxs
