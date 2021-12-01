a, b = map(int, input().split())
patients = list(map(int, input().split()))

q = [(i, v) for i, v in enumerate(patients)]
cnt = 0
while q:
    cur = q.pop(0)
    if any(cur[1] < c[1] for c in q):
        q.append(cur)
    else:
        cnt += 1
        if cur[0] == b:
            print(cnt)
            break
