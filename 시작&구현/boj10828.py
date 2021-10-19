import sys


def push(x):
    stack.append(x)


def pop():
    return stack.pop() if stack else -1


def size():
    return len(stack)


def empty():
    return 0 if stack else 1


def top():
    return stack[-1] if stack else -1


stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'top':
        print(top())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'pop':
        print(pop())
