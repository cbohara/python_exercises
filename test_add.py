import pytest
from add import add

def test_add_two_matrix_two_inner():
	matrix1 = [[1, -2], [-3, 4]]
	matrix2 = [[2, -1], [0, -1]]
	assert add(matrix1, matrix2) == [[3, -3], [-3, 3]]

def test_add_two_matrix_three_inner():
	matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
	matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
	assert add(matrix1, matrix2) == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]