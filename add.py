"""
def add(matrix1, matrix2):
	output = []
	for i, inner_matrix in enumerate(matrix1):
		added = []
		for j, value in enumerate(inner_matrix):
			current_value = inner_matrix[j]
			other_value = matrix2[i][j]
			added.append(current_value + other_value)
		output.append(added)
	return output
"""

def add(matrix1, matrix2):
	output = []
	for index in range(len(matrix1)):
		combos = list(zip(matrix1[index], matrix2[index]))
		sums = [sum(value) for value in combos]
		output.append(sums)
	return output

matrix1 = [
	[1, -2],
	[-3, 4]
]
matrix2 = [
	[2, -1],
	[0, -1]
]
#output = [[3, -3], [-3, 3]]
add(matrix1, matrix2)
