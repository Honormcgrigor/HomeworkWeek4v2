shop = {'hiking boots': 27.50,
        'tent': 49.00,
        'rucksack': 150,
        'sleeping bag': 89}

print(f'Welcome! The available items to purchase are \n {shop}. ')
def optional_exit_function():
    optional_exit = input(
        'If you would like to exit the shop, type exit. Otherwise, please press enter and continue browsing.')
    if optional_exit == 'exit':
        raise SystemExit
    else:
        return(print(f'The available items to purchase are \n {shop}. '))
optional_exit_function()

customer_budget = int(input('What is your budget? '))
what_to_buy = input('Which item would you like to buy? ')
def item_in_stock(what_to_buy):
    try:
        print(f'You have chosen {what_to_buy}. The price of this item is {shop[what_to_buy]}.')
    except KeyError:  # for some reason this should be a value error could do if KeyError, raise ValueError?
        (print('That item is not in the shop.'))
item_in_stock(what_to_buy)
def attempts_function(what_to_buy, customer_budget):
    class TooManyAttemptsError(Exception):
        pass
    attempts = 0
    while attempts < 3:
        try:
            try:
                if shop[what_to_buy] > customer_budget:
                    raise ValueError
                else:
                    print('Here is your item!')
                    raise SystemExit
            except ValueError:
                print('This item appears to be over your budget.')
                more_money = input(
                    'Do you have more money? If so, please enter the amount you would like to add to your budget. ')
                customer_budget += int(more_money)
                attempts += 1
        except TooManyAttemptsError:
            print('You do not have enough money.')
            raise SystemExit
attempts_function(what_to_buy, customer_budget)