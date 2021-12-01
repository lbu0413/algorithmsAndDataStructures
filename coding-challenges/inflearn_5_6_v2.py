from collections import deque

a, b = map(int, input().split())

prince_list = deque([i for i in range(1, a+1)])


cnt = 1
while len(prince_list) > 1:
    if cnt == 3:
        prince_list.popleft()
        cnt = 1
    else:
        prince_list.append(prince_list.popleft())
        cnt += 1

print(prince_list[0])
