from collections import defaultdict

def group_by(iterable, key_func):
	d = defaultdict(list)
	for x in iterable:
		d[key_func(x)].append(x)
	return d
