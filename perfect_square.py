#!/usr/bin/env python3

def is_perfect_square(n):
	digits = str(n)
	if digits[0] == '-':
		return False
	if digits[-1] in ['2', '3', '7', '8']:
		return False
	digits = digits.rstrip('0')

	while True:
		digits = [int(x) for x in digits]
		digital_root = sum(digits)
		if len(str(digital_root)) > 1:
			break
		else:
			digits = list(str(digital_root))

print(is_perfect_square(1091200))
