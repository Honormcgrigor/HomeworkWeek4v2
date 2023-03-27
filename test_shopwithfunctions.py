# Test 1:
from unittest import TestCase
from shopwithfunctions import shop, what_to_buy, optional_exit_function, item_in_stock, attempts_function, customer_budget

class TestingShop(TestCase):
    def test_exit(self):
     expected = 'exit'
     result = SystemExit
     self.assertEqual(expected, result)

    def test_in_dictionary(self):
        expected = KeyError
        result = item_in_stock('abcde')
        self.assertNotIn(self, expected, shop, msg='That item is not in the shop.')

    def test_in_budget(self):
        expected = ValueError
        result = attempts_function('tent', 20)
        self.assertGreater(customer_budget, shop[what_to_buy])