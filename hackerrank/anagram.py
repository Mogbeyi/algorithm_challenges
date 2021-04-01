#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the anagram function below.
lower_case_letters = string.ascii_lowercase
def anagram(s):
    first_half = s[len(s) // 2:]
    second_half = s[:len(s) // 2]
    minimum_count = 0
    letter_count_freq = form_count_freq(second_half)
    
    if len(first_half) != len(second_half):
        return -1
    elif first_half == second_half:
        return 0
    
    for char in first_half:
        index = lower_case_letters.index(char)
        if letter_count_freq[index] == 0:
            minimum_count += 1
        elif letter_count_freq[index] > 0:
            letter_count_freq[index] -= 1
        elif letter_count_freq[index] <= 0:
            minimum_count += 1
            
    return minimum_count

def form_count_freq(string):
    letter_freq = [0] * 26
    
    for char in string:
        index = lower_case_letters.index(char)
        letter_freq[index] += 1
        
    return letter_freq
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
