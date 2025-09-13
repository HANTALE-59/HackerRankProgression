#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# 

def plusMinus(arr) -> None: #//Complexity: O(n)
        
    plus_total = 0
    minus_total = 0
    zero_total = 0
    
    for e in arr:
        if  e > 0:
            plus_total +=1
        elif e < 0:
            minus_total += 1
        elif e == 0:
            zero_total += 1
    lenght = len(arr)
    
    print(round(plus_total/lenght,6))
    print(round(minus_total/lenght,6))
    print(round(zero_total/lenght,6))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
