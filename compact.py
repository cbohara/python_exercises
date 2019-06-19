def compact(iterable):
	"""
	Write a function that accepts an iterable and returns a new iterable with adjacent duplicate values removed
	:param iterable: iterable with duplicate values
	:return: iterable with adjacent duplicate values removed
	"""
	iterable = iter(iterable)
	try:
		previous = next(iterable)
	except StopIteration:
		return iter([])
	else:
		yield previous
		for current in iterable:
			if current == previous:
				continue
			else:
				yield current
			previous = current
