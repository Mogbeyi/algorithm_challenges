#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if can_replicate(magazine, note):
        print("Yes")
    else:
        print("No")

def can_replicate(first_array, second_array):
    magazine_word_freq = Counter(first_array)
    note_word_freq = Counter(second_array)

    for elem in note_word_freq.keys():
        if elem not in magazine_word_freq:
            return False
        elif note_word_freq[elem] > magazine_word_freq[elem]:
            return False

    return True

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

