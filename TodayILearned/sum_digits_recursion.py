# def sum_digit(n):
#     if n < 0:
#         ValueError('Inputs 0 or greater only!')
#     result = 0
#     while n is not 0:
#         result += n % 10
#         n = n // 10
#     return result + n


# 풀어보기


# recursive code
def sum_digits(n):
    if n < 0:
        ValueError('Inputs 0 or greater only!')
    if n <= 9:
        return n
    else:
        last_digit = n % 10
        return sum_digits(n // 10) + last_digit


print(sum_digits(499))
