from collections import deque


must = input()
n = int(input())

for i in range(n):
    classes = input()
    dq = deque(must)
    for j in classes:
        if j in dq:
            if j != dq.popleft():
                print(f"#{i+1} NO")
                break
    else:
        if dq:
            print(f"#{i+1} NO")
        else:
            print(f"#{i+1} YES")
