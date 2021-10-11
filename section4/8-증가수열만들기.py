import sys

sys.stdin = open('8-input.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))

lt = 0
rt = n-1
temp = []
res = ""
last = 0

while lt <= rt:
    if numbers[lt] > last:
        temp.append((numbers[lt], 'L'))
    if numbers[rt] > last:
        temp.append((numbers[rt], 'R'))
    temp.sort()
    if len(temp) == 0:
        break
    res += temp[0][1]
    last = temp[0][0]
    if res[-1] == 'L':
        lt += 1
    else:
        rt -= 1
    temp.clear()
print(len(res))
print(res)
