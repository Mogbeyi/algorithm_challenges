def build_hash_table(string):
    hash_table = {}

    for char in string:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1

    return hash_table

def make_anagrams(first, second):
    first_hash = build_hash_table(first)
    second_hash = build_hash_table(second)
    combined_string_length = len(first) + len(second)

    for char in first_hash.keys():
        if char in second_hash:
            total = first_hash[char] + second_hash[char]
            combined_string_length -= total 
            
    return combined_string_length

print(make_anagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'))
print(make_anagrams('abc', 'cde'))

#
#def main():
#    assert make_anagrams('abc', 'cde') == 4 
#    assert make_anagrams('abc', 'amnop') == 6 
#    assert make_anagrams('aaa', 'aaabb') == 2 
#    assert make_anagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa') == 4 
#
#main()
