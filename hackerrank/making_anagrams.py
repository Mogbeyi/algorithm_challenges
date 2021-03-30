from collections import Counter

def make_anagrams(s1, s2):
    smaller_string = s1 if len(s1) <= len(s2) else s2
    bigger_string = s2 if len(s2) >= len(s1) else s1
    bigger_string_freq = Counter(bigger_string)
    number_of_deletions = 0

    for char in smaller_string:
        if char in bigger_string_freq and bigger_string_freq[char] != 0:
            bigger_string_freq[char] -= 1
        else:
            number_of_deletions += 1
            
    return number_of_deletions + sum(bigger_string_freq.values())

def main():
   assert make_anagrams('abc', 'cde') == 4 
   assert make_anagrams('abc', 'amnop') == 6 
   assert make_anagrams('aaa', 'aaabb') == 2 
   assert make_anagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa') == 19

main()
