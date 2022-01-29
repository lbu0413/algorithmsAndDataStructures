
n = int(input())
nums = list(map(int, input().split()))
total = sum(nums)


def DFS(l, all_sum):
    if l == n:
        if all_sum == total-all_sum:
            print(all_sum, 'YES')

    else:
        DFS(l+1, all_sum+nums[l])
        DFS(l+1, all_sum)


DFS(0, 0)
