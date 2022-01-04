

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

add = 0
cnt = 0
for i in range(m):
    for j in range(k):
        add += nums[0]
        cnt += 1
    add += nums[1]
    cnt += 1
    if cnt == m:
        break


print(add)
