import sys
from collections import deque

sys.stdin = open('7-input.txt', 'r')

n, m = map(int, input().split())
weights = list(map(int, input().split()))

# pop(0)은 비효율적인 연산을 일으키므로 dequeue를 쓴다.
# weights.sort()
# cnt = 0
# while weights:
#     if len(weights) == 1:
#         cnt += 1
#         break
#     if weights[0] + weights[-1] > m:
#         weights.pop()
#         cnt += 1
#     else:
#         weights.pop(0)
#         weights.pop()
#         cnt += 1
# print(cnt)

weights.sort()
weights = deque(weights)
cnt = 0
while weights:
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] > m:
        weights.pop()
        cnt += 1
    else:
        weights.popleft()
        weights.pop()
        cnt += 1
print(cnt)
