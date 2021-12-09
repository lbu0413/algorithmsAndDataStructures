n = int(input())


cnt = [0]*(n+1)


def dfs(v):
    if v > n:
        for i in range(1, n+1):
            if cnt[i] == 1:
                print(i, end=" ")
        print()
    else:
        cnt[v] = 1
        dfs(v+1)
        cnt[v] = 0
        dfs(v+1)


print(dfs(1))
