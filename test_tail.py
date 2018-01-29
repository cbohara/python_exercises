#!/usr/bin/env python3
import pytest
from tail import tail

def test_list_zero():
	assert tail([1, 2], 0) == []

def test_list_one():
	assert tail([1, 2], 1) == [2]

def test_list_two():
	assert tail([1, 2], 2) == [1, 2]

def test_list_three():
	assert tail([1, 2, 3, 4, 5], 3) == [3, 4, 5]

def test_list_n_greater_then_input_len():
	assert tail([1, 2, 3, 4], 5) == [1, 2, 3, 4]

def test_list_negative_n():
	assert tail([1, 2, 3, 4], -5) == []

def test_string_zero():
	assert tail('hello', 0) == []

def test_string_one():
	assert tail('hello', 1) == ['o']

def test_string_two():
	assert tail('hello', 2) == ['l', 'o']

def test_string_negative_n():
	assert tail('hello', -2) == []

def test_tuple_zero():
	assert tail((1, 2, 3), 0) == []

def test_tuple_one():
	assert tail((1, 2, 3), 1) == [3]

def test_tuple_two():
	assert tail((1, 2, 3), 2) == [2, 3]

def test_tuple_negative_n():
	assert tail((1, 2, 3), -11) == []

def test_generator():
	squares = (n**2 for n in range(10))
	assert tail(squares, 3) == [49, 64, 81]
