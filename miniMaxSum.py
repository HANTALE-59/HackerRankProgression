#!/bin/python3
#https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
import math
import os
import re
import sys



def miniMaxSum(arr) -> str:
    arr.sort()
    return (f'{sum(arr[:4])} {sum(arr[-4:])}')




    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))
