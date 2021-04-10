import unittest


def has_palindrome_permutation(the_string):
    if len(the_string) < 2:
        return True
    
    freq_counter = count_chars(the_string)
    odd_count = 0
    
    for char in the_string:
        if is_odd(freq_counter[char]):
            odd_count += 1
            
    if odd_count >= 2:
        return False
    else:
        return True
    
def is_odd(x):
    return x % 2 != 0
    
def count_chars(string):
    counter = {}
    
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter

    

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
