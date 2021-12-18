def findDuplicate(nums):

    # start hopping from Node_0
    slow, fast = 0, 0

    # for locating start node of cycle
    check = 0

    # step1
    # cycle detection
    # let slow jumper and fast jumper meet somewhere in the cycle

    while True:
        # slow jumper hops 1 step, while faster jumper hops 2 steps fowrad.
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # step2
    # locate the start node of cycle
    # (ex) duplicate number

    while True:
        slow = nums[slow]
        check = nums[check]

        if slow == check:
            break

    return check


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))
