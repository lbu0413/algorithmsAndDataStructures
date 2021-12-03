a = input()
b = input()

hsh = dict()
for i in a:
    hsh[i] = 1

for j in b:
    if j not in hsh.keys():
        print('NO')
        break
    else:
        hsh[j] = 0

for key, value in hsh.items():
    if value != 0:
        print('NO')
        break
else:
    print('YES')

print(hsh)
