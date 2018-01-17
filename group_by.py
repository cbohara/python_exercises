from collections import defaultdict

def default(x):
	return x

def group_by(iterable, key_func=default):
	d = defaultdict(list)
	for x in iterable:
		d[key_func(x)].append(x)
	return d
