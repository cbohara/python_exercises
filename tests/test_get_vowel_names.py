#!/usr/bin/env python3
import pytest
from get_vowel_names import get_vowel_names

def test_one_vowel_name():
	names = ["Alice", "Bob", "Christy", "Jules"]
	assert get_vowel_names(names) == ["Alice"]

def test_no_vowel_name():
	names = ["Bob", "Christy", "Jules"]
	assert get_vowel_names(names) == []

def test_many_vowel_name():
	names = ["Adam", "Eve", "Oliver"]
	assert get_vowel_names(names) == ["Adam", "Eve", "Oliver"]
