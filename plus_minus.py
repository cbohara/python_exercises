#!/bin/python3

import math
import os
import random
import re
import sys


def format_output(number_input, desired_length=8):
    """
    0.666666 > 0.666666 -  length 8 
    0.5 > 0.500000 - length 3
    0.342 > 0.342000 - length 5
    """
    rounded_number = round(number_input, 6)
    str_number = str(rounded_number)
    if len(str_number) == desired_length:
        return str_number
    
    # 3
    len_str_number = len(str_number)
    # 8 - 3 = 5
    to_be_filled = desired_length - len_str_number
    to_be_added = '0' * to_be_filled
    return str_number + to_be_added
    

def plusMinus(input_list):
    count_positive = 0
    count_negative = 0
    count_zero = 0

    total_input = len(input_list)
    for number in input_list:
        if number > 0:
            count_positive += 1
        elif number < 0:
            count_negative += 1
        else:
            count_zero += 1

    ratio_positive = count_positive / total_input
    ratio_negative = count_negative / total_input
    ratio_zero = count_zero / total_input

    final_positive = format_output(ratio_positive)
    final_negative = format_output(ratio_negative)
    final_zero = format_output(ratio_zero)
    print(final_positive)
    print(final_negative)
    print(final_zero)
    

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)