import sys
n = int(sys.stdin.readline())

for i in range(n):
    length, target = list(map(int, sys.stdin.readline().split()))
    nums = list(map(int, sys.stdin.readline().split()))

    answer = 0
    queue = [(index, value) for index, value in enumerate(nums)]
    while True:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == target:
                print(answer)
                break
