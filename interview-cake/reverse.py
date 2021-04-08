import unittest


def reverse(list_of_chars):
    return reverse_copy(list_of_chars)

def reverse_copy(list_of_chars):
    if not list_of_chars:
        return []
    elif len(list_of_chars) == 1:
        return list_of_chars

    start = 0
    end = len(list_of_chars) - 1

    while start < end:
        temp = list_of_chars[start]
        list_of_chars[start] = list_of_chars[end]
        list_of_chars[end] = temp
        start += 1
        end -= 1

    return list_of_chars 


# Tests


class Test(unittest.TestCase):
    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ["A"]
        reverse(list_of_chars)
        expected = ["A"]
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ["A", "B", "C", "D", "E"]
        reverse(list_of_chars)
        expected = ["E", "D", "C", "B", "A"]
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
