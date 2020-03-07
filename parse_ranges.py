def parse_ranges(num_ranges):
	"""
	Transform string containing ranges of numbers into an iterable of those numbers

	Args:
		num_ranges (string) contains csv string representing ranges of numbers

	Returns:
		list of integers
	"""
	output = []
	for num_range in num_ranges.split(','):
		start, end = [int(x) for x in num_range.split('-')]
		num_range = list(range(start, end+1))
		output.extend(num_range)
	return output
