#!/usr/bin/env python3
import pytest
from anagram import is_anagram

def test_is_anagram_true_simple():
	assert is_anagram("tea", "eat") == True

def test_is_anagram_false_simple():
	assert is_anagram("tea", "treat") == False

def test_is_anagram_true_mixed_case():
	assert is_anagram("Listen", "silent") == True

def test_is_anagram_false_mixed_case():
	assert is_anagram("unicorn", "MaGiC") == False

def test_is_anagram_true_ignore_space():
	assert is_anagram("coins kept", "in pockets") == True

def test_is_anagram_false_ignore_space():
	assert is_anagram("what a day", "bicycle all day") == False

def test_is_anagram_true_ignore_punctuation():
	assert is_anagram("a diet", "I'd eat") == True

def test_is_anagram_false_ignore_punctuation():
	assert is_anagram("Happy New Years!", "Happy Birthday!!") == False

@pytest.mark.skip(reason="need to figure out how to deal with latin characters")
def test_is_anagram_true_ignore_latin_char():
	assert is_anagram("cardiografía", "radiográfica") == True

@pytest.mark.skip(reason="need to figure out how to deal with latin characters")
def test_is_anagram_true_ignore_latin_char():
	assert is_anagram("joyería", "radiográfica") == False
