#!/usr/bin/env python3
import pytest
from perfect_square import is_perfect_square

def test_small_numbers():
	assert is_perfect_square(4) == True
	assert is_perfect_square(16) == True
	assert is_perfect_square(11) == False
	assert is_perfect_square(26) == False

def test_large_numbers():
	assert is_perfect_square(1586375448590241) == True
	assert is_perfect_square(1420958445736851) == False

def test_nonreal_numbers():
	assert is_perfect_square(4.5) == False
	assert is_perfect_square(-4) == False

def test_raises_exception_for_str_arg():
	with pytest.raises(TypeError):
		is_perfect_square('4')
