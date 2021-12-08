# 1. 전위순회출력 - root 노트를 먼저 탐색 < 부모 -> 왼쪽 -> 오른쪽 >
# 2. 중위순회출력 - root 노트를 중간 순서로 탐색 < 왼쪽 -> 부모 -> 오른쪽 >
# 3. 후위순회출력 - root 노트를 마지막에 탐색 < 왼쪽 -> 오른쪽 -> 부모 >

n = int(input())


def dfs(n):
    if n > 7:
        return
    else:
        print(n, end=" ")
        dfs(n*2)
        dfs(n*2+1)


def dfs2(n):
    if n > 7:
        return
    else:
        dfs2(n*2)
        print(n, end=" ")
        dfs2(n*2+1)


def dfs3(n):
    if n > 7:
        return
    else:
        dfs3(n*2)
        dfs3(n*2+1)
        print(n, end=" ")


if __name__ == "__main__":
    dfs2(1)
