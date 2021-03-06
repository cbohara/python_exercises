import pytest
from add import add


def test_add_two_matrix_size_two():
	matrix1 = [[1, -2], [-3, 4]]
	matrix2 = [[2, -1], [0, -1]]
	assert add(matrix1, matrix2) == [[3, -3], [-3, 3]]


def test_add_two_matrix_size_three():
	matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
	matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
	assert add(matrix1, matrix2) == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]


def test_add_three_matrix_size_two():
	matrix1 = [[1, 9], [7, 3]]
	matrix2 = [[5, -4], [3, 3]]
	matrix3 = [[2, 3], [-3, 1]]
	assert add(matrix1, matrix2, matrix3) == [[8, 8], [7, 7]]


def test_add_uneven_matrices_raise_exception():
	with pytest.raises(ValueException):
		add([[1, 9], [7, 3]], [[1, 2], [3]])
