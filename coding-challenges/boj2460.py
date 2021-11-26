

cnt = 0
max_cnt = 0
for i in range(10):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
