def compact(iterable):
	"""
	Write a function that accepts an iterable and returns a new iterable with adjacent duplicate values removed
	:param iterable: iterable with duplicate values
	:return: iterable with adjacent duplicate values removed
	"""
	previous = object()
	for current in iterable:
		if current != previous:
			yield current
			previous = current
