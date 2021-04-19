import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    '''
      Take Out Orders: [1, 3, 5]
      Dine In Orders: [1, 4, 6]
      Served Orders: [1, 2, 4, 6, 5, 3]
      a_pointer = 0
      list = [1, 2]
    '''

    served_pointer, take_out_pointer, dine_in_pointer = 0, 0, 0

    while served_pointer < len(served_orders):
        if len(take_out_orders) + len(dine_in_orders) != len(served_orders):
            return False
        if take_out_pointer == len(take_out_orders) and dine_in_pointer == len(dine_in_orders):
            break

        if take_out_pointer < len(take_out_orders) and take_out_orders[take_out_pointer] == served_orders[served_pointer]:
            take_out_pointer += 1
            served_pointer += 1
        elif dine_in_pointer < len(dine_in_orders) and dine_in_orders[dine_in_pointer] == served_orders[served_pointer]:
            dine_in_pointer += 1
            served_pointer += 1
        else:
            return False

    return True


# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)

