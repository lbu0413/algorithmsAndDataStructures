n = int(input())
field = [list(map(int, input().split())) for i in range(n)]
m = int(input())

for i in range(m):
    a, b, c = map(int, input().split())
    for j in range(c):
        if b == 0:
            field[a-1].append(field[a-1].pop(0))
        elif b == 1:
            field[a-1].insert(0, field[a-1].pop())

add = 0
left = 0
right = n-1
for i in range(len(field)):
    for j in range(left, right+1):
        add += int(field[i][j])
    if i < n//2:
        left += 1
        right -= 1
    else:
        left -= 1
        right += 1

print(add)
