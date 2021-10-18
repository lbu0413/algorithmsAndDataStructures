# n = int(input())

# for i in range(n):
#     print((' ' * (n-i)) + ('*' * (i + 1)))

n = int(input())
for i in range(n):
    print(('*' * (i+1)).rjust(n))
