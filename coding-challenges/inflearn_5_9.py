from collections import deque


n = int(input())

dq = deque([])
for i in range(n):
    word = input()
    dq.append(word)

for i in range(n-1):
    word2 = input()
    for j in range(len(dq)):
        if dq[j] == word2:
            dq.popleft()
        else:
            dq.append(dq.popleft())
        break

print(dq[0])
