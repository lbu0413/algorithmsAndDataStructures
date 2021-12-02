from collections import deque

must = input()
tc = int(input())

for i in range(tc):
    ans = ""
    classes = deque(input())
    while classes:
        if classes[0] in must:
            if classes[0] in ans:
                classes.popleft()
            else:
                ans += classes.popleft()
        else:
            classes.popleft()
    if ans == must:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
