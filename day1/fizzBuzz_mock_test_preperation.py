#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n): #// Complexity: O(n)
    # Write your code here
    if n > 0:
        plus = 1
    else:
        plus = -1
    i = 0
    while True:
        i += plus
        if i %3==0 and i %5==0:
            print("FizzBuzz")
        elif i %3==0 and i %5!=0:
            print("Fizz")
        elif i %5==0 and i %3!=0:
            print("Buzz")
        else:
            print(i)
        if i >= n:
            break

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

