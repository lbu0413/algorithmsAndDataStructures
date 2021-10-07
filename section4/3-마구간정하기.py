import sys

n, c = map(int, sys.stdin.readline().split())

house = []
for i in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

start = house[0]
end = max(house)


def Checker(x):
    cnt = 1
    first = house[0]
    for i in range(1, len(house)):
        if house[i] >= first + x:
            cnt += 1
            first = house[i]
    return cnt


res = 0
while start <= end:
    mid = (start + end) // 2
    if Checker(mid) >= c:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print('ans: ', res)
