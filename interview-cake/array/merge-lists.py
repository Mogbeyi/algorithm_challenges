import unittest


def merge_lists(my_list, alices_list):
    my_list_pointer = 0
    alices_list_pointer = 0
    my_list_length = len(my_list)
    alices_list_length = len(alices_list)
    merged_result = []

    while my_list_pointer < my_list_length or alices_list_pointer < alices_list_length:
        if my_list_pointer == my_list_length:
            merged_result += alices_list[alices_list_pointer:]
            break
        elif alices_list_pointer == alices_list_length:
            merged_result += my_list[my_list_pointer:]
            break

        if my_list[my_list_pointer] <= alices_list[alices_list_pointer]:
            first_result = my_list[my_list_pointer]
            merged_result.append(first_result)
            my_list_pointer += 1
        elif alices_list[alices_list_pointer] < my_list[my_list_pointer]:
            second_result = alices_list[alices_list_pointer]
            merged_result.append(second_result)
            alices_list_pointer += 1

    return merged_result


class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
