n = int(input())
checker = [0] * (n+1)


def DFS(x):
    if x > n:
        for i in range(len(checker)):
            if checker[i] == 1:
                print(i, end=" ")
        print()
    else:
        checker[x] = 1
        DFS(x+1)
        checker[x] = 0
        DFS(x+1)


DFS(1)
