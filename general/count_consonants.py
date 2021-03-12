def tail_recursive_count_consonant(string, index, consonant_count):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if len(string) == index + 1:
        return consonant_count 
    elif string[index] not in vowels:
        return tail_recursive_count_consonant(string, index + 1, consonant_count + 1)
    else:
        return tail_recursive_count_consonant(string, index + 1, consonant_count)

def count_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if len(string) == 0:
        return 0
    elif string[0] not in vowels:
        return 1 + count_consonants(string[1:])
    else:
        return count_consonants(string[1:])

print(count_consonants('hello'))
print(tail_recursive_count_consonant('hello', 0, 0))
