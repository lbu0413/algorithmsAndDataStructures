a = input()
b = input()

hsh = dict()

for i in a:
    hsh[i] = hsh.get(i, 0) + 1

for i in b:
    hsh[i] = hsh.get(i, 0) - 1

for i in a:
    if hsh.get(i) > 0:
        print('NO')
        break
else:
    print('YES')
