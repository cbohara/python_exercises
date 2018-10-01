from datetime import datetime


def string_to_datetime(date_string):
	return datetime.strptime(date_string, "%m/%d/%Y")

def datetime_to_string(datetime_object):
	return datetime.strftime(datetime_object, "%m/%d/%Y")

def get_earliest(*date_strings):
	dates = [string_to_datetime(date) for date in date_strings]
	dates.sort()
	earliest_date = dates[0]
	return datetime_to_string(earliest_date)
