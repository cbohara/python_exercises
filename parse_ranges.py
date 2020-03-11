import re


PAIRS_REGEX = re.compile(r'(\d+)-(\d+)')


def parse_ranges(ranges_string):
	"""
	Transform string containing ranges of numbers into an iterable of those numbers

	Args:
		ranges_string (string) contains csv string representing ranges of numbers

	Returns:
		list of integers
	"""
	return [
		num
		for start, end in PAIRS_REGEX.findall(ranges_string)
		for num in range(int(start), int(end)+1)
	]
