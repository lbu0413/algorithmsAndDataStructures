# 풀이도움 https://art-coding3.tistory.com/40

import sys

T = int(input())

for i in range(T):
    line = sys.stdin.readline().split()
    for j in line:
        print(j[::-1], end=" ")
    print()
