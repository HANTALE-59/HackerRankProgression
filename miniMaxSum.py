#!/bin/python3
#https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def bubble_sorting2(lst) -> list :
    n = len(lst)
    changed = True

    while changed:
        changed = False
        for i in range(n - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                changed = True
        n -= 1
    return lst

def miniMaxSum(arr) -> None:
    
    arr = bubble_sorting2(lst=arr)
    print(f"{sum(arr[:4])} {sum(arr[-4:])}")


    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
