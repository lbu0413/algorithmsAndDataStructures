n, k = map(int, input().split())


cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
    else:
        n = n - 1
    print(n)
    cnt += 1

print(cnt)
