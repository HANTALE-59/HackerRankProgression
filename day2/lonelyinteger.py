#!/bin/python3
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a): #// Complexity: O(n²)
    # Write your code here
    for e in  a:
        occurence = a.count(e)
        if occurence == 1:
            return e
            
def lonelyinteger_beter(a): # O (n + n)
    counts = {}
    for e in a:                  # O(n)
        counts[e] = counts.get(e, 0) + 1
    for e, c in counts.items():   # O(n)
        if c == 1:
            return e
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
