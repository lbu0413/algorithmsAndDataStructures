n = int(input())

checker = [0]*(n+1)


def DFS(v):
    if v == n+1:
        for i in range(len(checker)):
            if checker[i] == 1:
                print(i, end=" ")
        print("")
    else:
        checker[v] = 1
        DFS(v+1)
        checker[v] = 0
        DFS(v+1)


DFS(1)
