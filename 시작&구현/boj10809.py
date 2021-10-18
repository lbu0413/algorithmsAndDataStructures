

import string

alphabets = string.ascii_lowercase

s = input()
res = []
for i in range(len(alphabets)):
    if alphabets[i] in s:
        res.append(s.index(alphabets[i]))
    else:
        res.append(-1)

print(*res)
