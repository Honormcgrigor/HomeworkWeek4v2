
#work out how many classes there will be
def split_class(num_students):
    num_class = num_students // 30
    return num_class

# create a dictionary with the classes
def dictionary(num_class, num_students):
    class_key = [f'Class {x}' for x in range(num_class+1)]
    class_index = [num_students//num_class for x in range(num_students+1)]
    dict_class = dict(zip(class_key, class_index))
    return dict_class

# print out answer as required
def print_answer(num_class, dict_classes):
    output = print(f'Proposed Allocation: {num_class} classes \n {dict_classes}.')
    return output

def main():
    num_students = 57
    split_class(num_students)
    num_class = num_class
    dictionary(num_class, num_students)
    dict_classes = dict_classes
    print_answer(num_class, dict_classes)
    return output

print(main())

""" I had a lot of ideas about how to do this, but didn't have time to execute, or even fully make a code that runs.
I have included all my other ideas below:"""
# num_students = 58
# list_students1 = [1, 2, 3, 4, 5, 6]
# list_students2 = []

# def main(num_students):
#     split_class(num_students)
#     try:
#         if num_class == 1
#             print_answer(num_students, num_class)
#         elif num_class == 2
#             divide_into_two(list_students1)
#             count_class2(list_students1, list_students2)
#         elif 60 < num_students <= 90:
#     finally:

"""here, I wanted to try to create a try, finally, to divide the classes into the correct number """



# input - how many people are in the class

# def how_many_students(num_students):
#     num_students = int(input('How many students need to be divided into classes?'))

# minimum - split class into 2 - if less than 60, split into 2
"""Here, I tried to divide the students by iterating through the list, and then slicing the list, to get an even
amount in each class"""
# def get_all_students(num_students):
#     list_students1 = []
#     for i in range(num_students+1):
#         list_students1.append(i)
#     return list_students1

# def divide_into_two(list_students1):
#     list_students2 = list_students1[1::2]
#     return list_students2

# def count_class2(list_students1, list_students2):
#     class1 = len(list_students1)
#     class2 = len(list_students2)
#     return class1, class2


#def dictionary - put into dictionary
