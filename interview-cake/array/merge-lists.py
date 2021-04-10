import unittest


def merge_lists(my_list, alices_list):
    '''
    my_list     = [2, 4, 6, 8]
    alices_list = [1, 7]
    my_list_pointer = 4
    alices_list_pointer = 2
    merged_list = [1, 2, 4, 6, 7,8] 
    '''
    
    my_list_pointer = 0     #2
    alices_list_pointer = 0 #1
    my_list_length = len(my_list) #3 
    alices_list_length = len(alices_list) #3
    bigger_list_length = my_list_length if my_list_length > alices_list_length else alices_list_length #3
    merged_list = []  #[1, 3, 4, 5]


    while (my_list_pointer < bigger_list_length) or (alices_list_pointer < bigger_list_length):
            if my_list[my_list_pointer] <= alices_list[alices_list_pointer] and my_list_pointer < my_list_length:
                result = my_list[my_list_pointer]
                merged_list.append(result)
                if my_list_pointer != my_list_length:
                    my_list_pointer += 1
            if my_list[my_list_pointer] >= alices_list[alices_list_pointer] and alices_list_pointer < alices_list_length:
                second_result = alices_list[alices_list_pointer]
                merged_list.append(second_result)
                if alices_list_pointer != alices_list_length:
                    alices_list_pointer += 1

    return merged_list

print(merge_lists([2, 4, 6, 8], [1, 2, 3, 7]))


# Tests

# class Test(unittest.TestCase):

#     def test_both_lists_are_empty(self):
#         actual = merge_lists([], [])
#         expected = []
#         self.assertEqual(actual, expected)

#     def test_first_list_is_empty(self):
#         actual = merge_lists([], [1, 2, 3])
#         expected = [1, 2, 3]
#         self.assertEqual(actual, expected)

#     def test_second_list_is_empty(self):
#         actual = merge_lists([5, 6, 7], [])
#         expected = [5, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_both_lists_have_some_numbers(self):
#         actual = merge_lists([2, 4, 6], [1, 3, 7])
#         expected = [1, 2, 3, 4, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_lists_are_different_lengths(self):
#         actual = merge_lists([2, 4, 6, 8], [1, 7])
#         expected = [1, 2, 4, 6, 7, 8]
#         self.assertEqual(actual, expected)


# unittest.main(verbosity=2)