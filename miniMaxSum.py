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

# Utilise la fonction `.sort` de python
# Elle sera toujours plus perfommante que la tienne
# Par example bubble_sorting c'est O(n * n) alors que il y a des algos en O(log n * n) 


# def bubble_sorting2(lst) -> list :
#     n = len(lst)
#     changed = True

#     while changed:
#         changed = False
#         for i in range(n - 1):
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#                 changed = True
#         n -= 1
#     return lst

# C'est mieux si ta fonction retourne une valeur plutot que print
def miniMaxSum(arr) -> (int, int):
    arr.sort()
    return (sum(arr[:4]),sum(arr[-4:]))


    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(*miniMaxSum(arr))
