def twoSum(numbers, target):
    left, right = 0, len(numbers)-1

    while left < right:
        theNum = numbers[left] + numbers[right]

        if theNum == target:
            return [left+1, right+1]
        elif theNum < target:
            left += 1
        else:
            right -= 1
