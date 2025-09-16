#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k): #//Complexity: O(len(n)) d'après chat GPT
    n_str = str(n)
    if len(n_str) <=1:
        return(n)
    if k>0:
        n_str = str(sum(int(d) for d in n_str) * k)
    n = 0
    for e in n_str:
        n += int(e)
    return superDigit(n,k=0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
