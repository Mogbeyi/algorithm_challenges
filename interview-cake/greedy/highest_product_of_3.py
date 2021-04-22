import unittest
from functools import reduce


def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError("Less than 3 items!")
        
    max_candidates = list_of_ints[:3]
    min_candidates = list_of_ints[:3]
    
    for i, elem in enumerate(list_of_ints[3:]):
        min_value_of_max = min(max_candidates)
        max_value_of_min = max(min_candidates)
        min_idx_of_max = max_candidates.index(min_value_of_max)
        max_idx_of_min = min_candidates.index(max_value_of_min)
        
        if elem > min_value_of_max:
            max_candidates[min_idx_of_max] = elem
        elif elem < max_value_of_min:
            min_candidates[max_idx_of_min] = elem
            
    min_candidates = sorted(min_candidates)
            
    if list_product(max_candidates) > list_product(min_candidates[:2] + max_candidates[-1:]):
        return list_product(max_candidates)
    else:
        return list_product(min_candidates[:2] + max_candidates[-1:])
        

def list_product(arr):
    return reduce(lambda x, y: x * y, arr)

    
            

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)