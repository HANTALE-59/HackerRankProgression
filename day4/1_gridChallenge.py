#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid): #//Complexity: O(n^2 log(n))
    grid = ["".join(sorted(row)) for row in grid]#O(n log(n))
    #for e in grid:
    #    e.sort()
    length_grid = len(grid)
    length_row = len(grid[0])
    for i in range(0,length_row):
        for y in range(length_grid-1,0,-1):  #n -> parce que balaye chaque élément au final dans la double boucle
            if grid[y][i] < grid[y-1][i]:
                return "NO"
    return "YES"
            
        


grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywua']
print(gridChallenge(grid))
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
'''
