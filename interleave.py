#!/usr/bin/env python3

def interleave(*iterables):
	iterators = [iter(i) for i in iterables]
	while iterators:
		for iterator in iterators:
			try:
				yield next(iterator)
			except StopIteration:
				iterators.remove(iterator)
