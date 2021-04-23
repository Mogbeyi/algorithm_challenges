#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    min_distance = float('inf')
    freq_value = form_freq_value(a)
    flag = False
    
    for elem in a:
        if len(freq_value[elem]) > 1:
            min_distance = min(min_distance, abs(freq_value[elem][0] - freq_value[elem][1]))
            flag = True
        
    if flag:
        return min_distance
    else:
        return -1
    
def form_freq_value(arr):
    hash_table = {}
    
    for i, elem in enumerate(arr):
        if elem in hash_table:
            hash_table[elem] += [i]
        else:
            hash_table[elem] = [i]
        
    return hash_table
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
