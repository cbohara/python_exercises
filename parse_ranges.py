def partition(sep, group):
	"""
	Helper function wrapping around python string partition function

	Args:
		sep (string) used to separate range of numbers if applicable
		group (string) representings a number or a range of numbers
	Returns:
		tuple of integers for start and stop value for range function
	"""
	a, _, b = group.partition(sep)
	return ((int(a), int(b)) if b else (int(a), int(a)))


def parse_ranges(ranges_string):
	"""
	Transform string containing ranges of numbers into an iterable of those numbers

	Args:
		ranges_string (string) contains csv string representing ranges of numbers

	Returns:
		generator of single integers
	"""
	pairs = (
		partition('-', group)
		for group in ranges_string.split(',')
	)
	return (
		num
		for start, stop in pairs
		for num in range(start, stop+1)
	)
