# finding the minimum value in a list


# iterative code

# def find_min(my_list):
#     minimum = None
#     for element in my_list:
#         if not minimum or element < minimum:
#             minimum = element
#     return minimum


# recursive code
def find_min(my_list, minimum=None):
    if len(my_list) == 0:
        return minimum
    else:
        if minimum == None or minimum > my_list[0]:
            minimum = my_list[0]
    return find_min(my_list[1:], minimum)


my_list = [1, 4, 5, 6, 0, -4, 10]
print(find_min(my_list))
print(find_min([1000, 20, 3, 49, 785, 4]))
