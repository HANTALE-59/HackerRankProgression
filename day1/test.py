#!/bin/python3
#https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
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

def timeConversion(s) -> str:
    
    period = s[-2:]
    hour = s[:2]
    rest = s[2:-2]

    if period == "AM":
        if hour == "12":
            hour = "00"
    else:
        if hour == "12":
            hour = "00"
    return f"{hour}{rest}"

    

print(timeConversion(s='11.00.20PM'))
print(timeConversion(s='12.10.20PM'))
print(timeConversion(s='11.00.20AM'))
print(timeConversion(s='12.10.20AM'))