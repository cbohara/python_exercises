from datetime import datetime


def str_to_dt(date_str):
	return datetime.strptime(date_str, "%m/%d/%Y")

def get_earliest(date_str1, date_str2):
	date1 = str_to_dt(date_str1)
	date2 = str_to_dt(date_str2)
	if date1 < date2:
		return date_str1
	elif date2 < date1:
		return date_str2
	else:
		return date_str1
