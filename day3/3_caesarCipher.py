#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k): #//Complexity : O(n) //I had to do it in class so I new ord and chr things lol
    # Write your code here
    new_text = ""
    for char in str(s):
        if char.isalpha() :
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            new_ord = ((ord(char)-base)+k) %26
            char = chr(new_ord+base)
        new_text += char
    return new_text
        


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
