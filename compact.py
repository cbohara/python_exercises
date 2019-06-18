def compact(iterable):
	"""
	Write a function that accepts an iterable and returns a new iterable with adjacent duplicate values removed
	:param iterable: iterable with duplicate values
	:return: iterable with adjacent duplicate values removed
	"""
	output = []
	try:
		previous = iterable[0]
	except IndexError:
		return list()
	else:
		output.append(previous)
		for i in range(1, len(iterable)):
			current = iterable[i]
			if current == previous:
				continue
			else:
				output.append(current)
			previous = current
	return output


print(compact([1, 1, 2, 2, 3, 2]))
print(compact([1, 1, 1]))
