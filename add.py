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
