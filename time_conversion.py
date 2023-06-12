#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    am_or_pm = s[-2:]

    hour = int(s[:2])
    if am_or_pm == "AM":
        new_hour = hour - 12
    else:
        new_hour = hour + 12

    new_hour_fmt_str = str(new_hour).zfill(2)
    new_time = f'{new_hour_fmt_str}{s[2:-2]}'
    return new_time


if __name__ == '__main__':
    s = "12:01:00AM"
    result = timeConversion(s)
    print(result)

    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)