def with_previous(sequence):
	return zip(sequence, [None, *sequence])
