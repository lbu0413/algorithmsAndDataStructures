import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
print(weights)
cnt = 0
while weights:
    if len(weights) > 1:
        if weights[0] + weights[-1] <= m:
            weights.pop(0)
            weights.pop(-1)
        else:
            weights.pop(-1)
    else:
        weights.pop()
    cnt += 1

print(cnt)
