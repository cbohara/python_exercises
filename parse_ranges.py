def parse_ranges(ranges_string):
	"""
	Transform string containing ranges of numbers into an iterable of those numbers

	Args:
		ranges_string (string) contains csv string representing ranges of numbers

	Returns:
		list of integers
	"""
	for item in ranges_string.split(','):
		if item.isdigit():
			yield int(item)
		else:
			start, end = (int(num) for num in item.split('-'))
			for num in range(start, end+1):
				yield num
