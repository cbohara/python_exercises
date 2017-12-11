#!/usr/bin/env python3

def negate(matrix):
	output = []
	for row in matrix:
		out_row = []
		for number in row:
			if number < 0:
				out_row.append(abs(number))
			if number > 0:
				out_row.append(number - (number * 2))
		output.append(out_row)
	return output
