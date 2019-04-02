def add(matrix1, matrix2):
	output = []
	for index in range(len(matrix1)):
		combos = list(zip(matrix1[index], matrix2[index]))
		sums = [sum(value) for value in combos]
		output.append(sums)
	return output
