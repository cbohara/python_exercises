#!/usr/bin/env python3
import pytest
from negate import negate

def test_empty():
	assert negate([[],[]]) == [[],[]]

def test_single_row():
	assert negate([[-1, 1, 2, 3, -6]]) == [[1, -1, -2, -3, 6]]

def test_two_rows():
	assert negate([[-1, 1, 2, 3, -6], [5, 0, -10, 2]]) == [[1, -1, -2, -3, 6], [-5, 0, 10, -2]]
