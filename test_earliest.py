import pytest
from earliest import get_earliest


def test_same_month_and_day():
	newer = "01/27/1832"
	older = "01/27/1756"
	assert get_earliest(newer, older) == older

def test_february_29th():
	newer = "02/29/1972"
	older = "12/21/1946"
	assert get_earliest(newer, older) == older

def test_smaller_month_bigger_day():
	newer = "03/21/1946"
	older = "02/24/1946"
	assert get_earliest(newer, older) == older

def test_same_month_and_year():
	newer = "06/24/1958"
	older = "06/21/1958"
	assert get_earliest(newer, older) == older

def test_two_invalid_dates():
	newer = "02/30/2006"
	older = "02/29/2006"
	with pytest.raises(ValueError):
		get_earliest(newer, older)

def test_many_dates():
	d1 = "01/24/2007"
	d2 = "01/21/2008"
	d3 = "02/21/2009"
	d4 = "05/11/2006"
	assert get_earliest(d1, d2, d3) == d1
	assert get_earliest(d1, d2, d3, d4) == d4
