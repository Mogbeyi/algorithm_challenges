from collections import Counter

def gameOfThrones(s):
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: x % 2 != 0
    s_freq = Counter(s)
    letter_count = 0
    
    for char in s_freq.keys():
        if is_odd(s_freq[char]):
            letter_count += 1
    
    if is_even(len(s)) and letter_count == 0:
        return "YES"
    elif is_odd(len(s)) and letter_count == 1:
        return "YES"
    else:
        return "NO"

print(gameOfThrones('aaabbbb'))