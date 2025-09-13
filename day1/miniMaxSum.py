#!/bin/python3
#https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
import math
import os
import re
import sys



def miniMaxSum(arr) -> str: #Complexity: O(n log(n))
    arr.sort() #O(n log(n)) askip
    return (f'{sum(arr[:4])} {sum(arr[-4:])}') #O(1)




    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))
