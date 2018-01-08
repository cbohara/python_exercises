#!/usr/bin/env python3

def interleave(*iterables):
	iterables = [list(x) for x in iterables]
	result = []
	for x in range(len(iterables[0])):
		for iterable in iterables:
			result.append(iterable[x])
	return result

nums = [1, 2, 3]
squares = (n*n for n in nums)
print(interleave(nums, squares))
