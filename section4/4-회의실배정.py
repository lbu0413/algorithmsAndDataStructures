import sys

n = int(sys.stdin.readline())

meetings = []

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))


meetings.sort(key=lambda x: x[1])


cnt = 0
first = 0
for i in range(len(meetings)):
    if meetings[i][0] >= first:
        cnt += 1
        first = meetings[i][1]
print(cnt)
