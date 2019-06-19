import sys


def compact(iterable):
	"""
	Write a function that accepts an iterable and returns a new iterable with adjacent duplicate values removed
	:param iterable: iterable with duplicate values
	:return: iterable with adjacent duplicate values removed
	"""
	iterable = iter(iterable)
	output = []
	try:
		previous = next(iterable)
	except StopIteration:
		return list()
	else:
		output.append(previous)
		for current in iterable:
			if current == previous:
				continue
			else:
				output.append(current)
			previous = current
	return output
