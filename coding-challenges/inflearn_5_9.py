

n = int(input())
hsh = {}

for i in range(n):
    word = input()
    hsh[word] = 1

for j in range(n-1):
    word = input()
    hsh[word] = 0

for key, value in hsh.items():
    if value == 1:
        print(key)
