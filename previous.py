def with_previous(sequence):
	output = []
	previous = None
	for index, item in enumerate(sequence):
		output.append((item, previous))
		previous = item
	return output
