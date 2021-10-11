import sys

n = int(sys.stdin.readline())

stats = []
for i in range(n):
    height, weight = map(int, sys.stdin.readline().split())
    stats.append((height, weight))

stats.sort(key=lambda x: x[1], reverse=True)
print(stats)
cnt = 1

max = stats[0]
for i in range(1, len(stats)):
    if stats[i][0] > max[0] or stats[i][1] > max[1]:
        cnt += 1
        max = stats[i]
print(cnt)
