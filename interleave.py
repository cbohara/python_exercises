#!/usr/bin/env python3

def interleave(*iterables):
	iterables = [list(x) for x in iterables]
	longest_iterable = sorted(iterables, reverse=True)[0]
	result = []
	for x in range(len(longest_iterable)):
		for iterable in iterables:
			try:
				result.append(iterable[x])
			except IndexError:
				continue
	return result
