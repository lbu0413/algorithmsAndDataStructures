
nums = []

for i in range(9):
    midget = int(input())
    nums.append(midget)

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if sum(nums) - nums[i] - nums[j] == 100:
            nums.pop(j)
            nums.pop(i)
            break
nums.sort()
for i in nums:
    print(i)
