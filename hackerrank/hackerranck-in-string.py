#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    const = 'hackerrank'
    count = 0
    pos = 0
    
    for i,char in enumerate(s):
        if pos == 10:
            break
        if char == const[pos]:
            pos += 1
            
    if pos == 10:
        return "YES"
    else:
        return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
