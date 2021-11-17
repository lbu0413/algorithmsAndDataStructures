import sys

n = int(sys.stdin.readline())
for i in range(n):
    length, target = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    queue = [(index, value) for index, value in enumerate(nums)]
    answer = 0
    while True:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == target:
                print(answer)
                break
