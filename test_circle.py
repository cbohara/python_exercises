#!/usr/bin/env python3
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
