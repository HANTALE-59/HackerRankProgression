#!/bin/python3
#https://www.hackerrank.com/test/4nahpm20m33/questions/di1dm3kpigj
import math
import os
import random
import re
import sys




visual_matrice = [
    [12, 85, 23, 45, 32, 42],

    [35, 64, 78, 53, 91, 27],

    [88, 14, 62, 39, 76, 58],

    [41, 95, 24, 67, 83, 19],

    [72, 56, 11, 98, 34, 65],

    [29, 47, 86, 54, 77, 31]
]


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flipp_lign(lign:list,n:int):
    lign.reverse()
    return
def calcul_highest(lign:list,n:int):
    if sum(lign[:n]) < sum(lign[n:]):
        return
    flipp_lign(lign=lign,n=n)
    
def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix[0])/2
    while True:
        for i, e in matrix:
            calcul_highest(lign=e,n=n)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
