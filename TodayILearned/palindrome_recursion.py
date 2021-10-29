# def is_palindrome(my_string):
#     string_length = len(my_string)
#     middle_index = string_length // 2
#     for index in range(0, middle_index):
#         opposite_index = string_length - index - 1
#         if my_string[index] != my_string[opposite_index]:
#             return False
#     return True
# print(is_palindrome('bravazrb'))
# print(is_palindrome('madam'))

def is_palindrome(my_string):
    if len(my_string) < 2:
        return True
    if my_string[0] != my_string[-1]:
        return False
    return is_palindrome(my_string[1:-1])


print(is_palindrome('madamm'))
print(is_palindrome('superepus'))
