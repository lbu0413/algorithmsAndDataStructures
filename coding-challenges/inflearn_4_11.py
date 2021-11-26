n = int(input())
nums = list(map(int, input().split()))

tmp = [0] * n

for i in range(n):
    for j in range(n):
        if nums[i] == 0 and tmp[j] == 0:
            tmp[j] = i+1
            break
        elif tmp[j] == 0:
            nums[i] -= 1
print(*tmp)
