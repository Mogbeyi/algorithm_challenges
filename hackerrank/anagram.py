#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the anagram function below.
def anagram(s):
    # 'xaxbbbxx'
    first_half = s[:len(s) // 2] # 'xaxb'
    second_half = s[len(s) // 2:] #'bbxx'
    minimum_characters = 0  # 1
    second_half_counter = Counter(second_half) #{b -> 2, x -> 0}
    
    if len(first_half) != len(second_half):
        return -1
    elif first_half == second_half:
        return 0
    
    for char in first_half:
        if char not in second_half_counter:
            minimum_characters += 1
        elif char in second_half_counter and second_half_counter[char] > 0:
            second_half_counter[char] -= 1
        elif char in second_half_counter and second_half_counter[char] <= 0:
            minimum_characters += 1
            
    return minimum_characters
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
