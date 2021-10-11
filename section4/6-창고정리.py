import sys

sys.stdin = open('6-input.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

numbers.sort()
for i in range(m):
    numbers[0] += 1
    numbers[-1] -= 1
    numbers.sort()

print(numbers[-1] - numbers[0])
