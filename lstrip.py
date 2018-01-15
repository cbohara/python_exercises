#!/usr/bin/env python3

def lstrip(iterable, obj):
	start = 0
	iterable = list(iterable)
	for index, value in enumerate(iterable):
		if value == obj:
			continue
		else:
			start = index
			break
	try:
		if start == 0 and iterable[0] == obj:
			return []
	except IndexError:
		return []
	else:
		return iterable[start:]
