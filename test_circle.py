#!/usr/bin/env python3
import pytest
import math
from circle import Circle

def test_radius():
	circle = Circle(5)
	assert circle.radius == 5

def test_default_radius():
	circle = Circle()
	assert circle.radius == 1

def test_diameter_changes():
	circle = Circle(2)
	assert circle.diameter == 4
	circle.radius = 3
	assert circle.diameter == 6

def test_area():
	circle = Circle(2)
	assert circle.area == math.pi * 4
	circle = Circle(1)
	assert circle.area == math.pi

def test_dynamic_radius():
	circle = Circle(2)
	assert circle.diameter == 4
	circle.diameter = 3
	assert circle.radius == 1.5

def test_no_negative_radius():
	circle = Circle(2)
	with pytest.raises(ValueError):
		circle.radius = -10

def test_equality():
	circleA = Circle(2)
	circleB = Circle(2)
	circleC = Circle(1)

	assert circleA == circleB
	assert circleB != circleC != circleA
	assert not circleA != circleB
	assert not circleA == circleC
	assert not circleB == circleC

	circleC.radius = 2
	assert circleA == circleB == circleC
	assert not circleB != circleC
	assert not circleA != circleC

def test_comparability():
	circleA = Circle(1)
	circleB = Circle(2)
	circleC = Circle(3)
	assert circleA < circleB < circleC
	assert circleA <= circleB <= circleC
	assert not circleB < circleA
	assert not circleC < circleB
	assert circleC > circleB > circleA
	assert circleC >= circleB >= circleA
	assert not circleA > circleB
	assert not circleB > circleC
