# 재귀함수를 이용한 이진수 출력
n = int(input())


def DFS(n):
    if n == 0:
        return
    else:
        DFS(n//2)
        print(n % 2, end="")


print(DFS(n))
