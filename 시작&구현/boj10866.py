import sys


def push_front(x):
    deque.insert(0, x)


def push_back(x):
    deque.append(x)


def pop_front():
    return deque.pop(0) if deque else -1


def pop_back():
    return deque.pop() if deque else -1


def size():
    return len(deque)


def empty():
    return 0 if deque else 1


def front():
    return deque[0] if deque else -1


def back():
    return deque[-1] if deque else -1


deque = []
n = int(sys.stdin.readline())

for i in range(n):
    deque_sample = sys.stdin.readline().split()
    if deque_sample[0] == "push_back":
        push_back(deque_sample[1])
    elif deque_sample[0] == "push_front":
        push_front(deque_sample[1])
    elif deque_sample[0] == "front":
        print(front())
    elif deque_sample[0] == 'back':
        print(back())
    elif deque_sample[0] == 'size':
        print(size())
    elif deque_sample[0] == 'empty':
        print(empty())
    elif deque_sample[0] == 'pop_front':
        print(pop_front())
    elif deque_sample[0] == 'pop_back':
        print(pop_back())
