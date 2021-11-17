
# Queue는 FIFO( First In First Out )

import sys


def push(x):
    queue.append(x)


def pop():
    return queue.pop(0) if queue else -1


def size():
    return len(queue)


def empty():
    return 0 if queue else 1


def front():
    return queue[0] if queue else -1


def back():
    return queue[-1] if queue else -1


queue = []
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'back':
        print(back())
    elif command[0] == 'empty':
        print(empty())
