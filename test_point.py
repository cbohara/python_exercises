import pytest
from point import Point


def test_attributes():
	point = Point(1, 2, 3)
	assert point.x == 1
	assert point.y == 2
	assert point.z == 3
	point.x = 4
	assert point.x == 4

def test_string_representation():
	point = Point(1, 2, 3)
	assert str(point) == 'Point(x=1, y=2, z=3)'
	assert repr(point) == 'Point(x=1, y=2, z=3)'
	point.y = 4
	assert str(point) == 'Point(x=1, y=4, z=3)'
	assert repr(point) == 'Point(x=1, y=4, z=3)'

def test_equality_and_inequality():
	p1 = Point(1, 2, 3)
	p2 = Point(1, 2, 4)
	p3 = Point(1, 2, 3)
	assert p1 != p2
	assert p1 == p3
	p3.x, p3.z = p3.z, p3.x
	assert p1 != p3

def test_shifting():
	p1 = Point(1, 2, 3)
	p2 = Point(4, 5, 6)
	p3 = p2 + p1
	p4 = p3 - p1
	assert (p3.x, p3.y, p3.z) == (5, 7, 9)
	assert (p4.x, p4.y, p4.z) == (p2.x, p2.y, p2.z)

def test_scale():
	p1 = Point(1, 2, 3)
	p2 = p1 * 2
	assert (p2.x, p2.y, p2.z) == (2, 4, 6)
	p3 = 3 * p1
	assert (p3.x, p3.y, p3.z) == (3, 6, 9)

def test_iterable_point():
	point = Point(x=1, y=2, z=3)
	x, y, z = point
	assert (x, y, z) == (1, 2, 3)
