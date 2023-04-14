

# input needed
# def what_word(word):
#     word = input('Insert your word: ')

# raise exception if it is not a string
# def must_be_string - this is only necessary if you don't use input

word = 'isogram'
# split word into letters - list
def split_word(word):
    letters = list(word)
    return letters

def num_letters(letters):
    count_list = []
    for l in letters:
        count_list.append(letters.count(l))
    return count_list

def there_are_no_repetitions(count_list):
    for x in count_list:
        if count_list.count(2) > 0 or count_list.count(3) > 0:
            return False
        else:
            return True


def main():
    word = 'isogram'
    split_word(word)
    letters = split_word(word)
    num_letters(letters)
    count_list = num_letters(letters)
    are_there_repetitions(count_list)
    return there_are_no_repetitions(count_list)

print(main())


# print(num_letters(['i', 's', 'o', 'g']))
#
if __name__ == '__main__':
    main()

# if each letter count = 0, true

#if one letter count = <0, false

