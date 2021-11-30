a, b = map(int, input().split())

q = [i for i in range(1, a+1)]

cnt = b-1
while len(q) > 1:
    q.pop(cnt)
    cnt += b-1
    if cnt >= len(q):
        cnt %= len(q)

print(q[0])
