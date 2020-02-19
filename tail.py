def tail(iterable, n):
	if n <= 0:
		return []

	print(iterable[-n:])


# [3, 4, 5]
tail([1, 2, 3, 4, 5], 3)

# ['l', 'o']
tail('hello', 2)
