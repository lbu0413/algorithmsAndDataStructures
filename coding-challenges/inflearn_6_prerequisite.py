

# def recursive(n):
#     if n < 1:
#         return 1
#     return n + recursive(n-1)


# print(recursive(3))
def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x, end=" ")


if __name__ == "__main__":
    n = int(input())
    DFS(n)
