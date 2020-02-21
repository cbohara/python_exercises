from collections import deque


def tail(iterable, n):
	if n <= 0:
		return []
	return list(deque(iterable, maxlen=n))
