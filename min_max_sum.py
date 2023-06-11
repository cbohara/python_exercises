#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    sorted_list = sorted(arr)
    min_sum = sum(sorted_list[:4])
    max_sum = sum(sorted_list[1:])
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)