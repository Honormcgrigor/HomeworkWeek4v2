# Test 1:
from unittest import TestCase
from test_shop.py import optional_exit_function()

# optional_exit = input('If you would like to exit the shop, type exit. Otherwise, please press enter and continue browsing.')
# if optional_exit == 'exit':
#     raise SystemExit
# else:
#     print(f'The available items to purchase are \n {shop}. ')
class TestExit(TestCase):
    def exit_test(self):
     expected = 'exit'
     result = optional_exit_function()
     self.assertEqual(expected, result)


# def remain_test(optional_exit):
#     if optional_exit != 'exit':
#         return True
#     return False

# Test 2:
# try:
#     print(f'You have chosen {what_to_buy}. The price of this item is {shop[what_to_buy]}.')
# except KeyError:  # for some reason this should be a value error could do if KeyError, raise ValueError?
#     print('That item is not in the shop.')

# Test 3: - break down into smaller blocks


# break down into : test 3:
# if shop[what_to_buy] > customer_budget:
#                 raise ValueError
#             else:
#                 print('Here is your item!')
#                 raise SystemExit

# test 4:
# try:
#             if shop[what_to_buy] > customer_budget:
#                 raise ValueError
#             else:
#                 print('Here is your item!')
#                 raise SystemExit
#         except ValueError:
#             print('This item appears to be over your budget.')
#             more_money = input('Do you have more money? If so, please enter the amount you would like to add to your budget. ')
#             customer_budget += int(more_money)
#             attempts += 1


# test 5:
# class TooManyAttemptsError(Exception):
#     pass
# attempts = 0
#
# while attempts < 3:
#     try:
#         try:
#             if shop[what_to_buy] > customer_budget:
#                 raise ValueError
#             else:
#                 print('Here is your item!')
#                 raise SystemExit
#         except ValueError:
#             print('This item appears to be over your budget.')
#             more_money = input('Do you have more money? If so, please enter the amount you would like to add to your budget. ')
#             customer_budget += int(more_money)
#             attempts += 1
#     except TooManyAttemptsError:
#         print('You do not have enough money.')
#         raise SystemExit