import sys

n, m = map(int, sys.stdin.readline().split())

lines = []

for i in range(n):
    each = int(sys.stdin.readline())
    lines.append(each)

start = 1
end = max(lines)
res = 0


def Checker(x):
    add = 0
    for i in range(len(lines)):
        add += (lines[i] // x)
    return add


while start <= end:
    mid = (start + end) // 2
    if (Checker(mid)) >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)
