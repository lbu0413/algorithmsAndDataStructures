n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

for i in range(len(board)):
    board[i].append(0)
    board[i].insert(0, 0)
board.insert(0, [0]*(n+2))
board.append([0]*(n+2))
print(board)
cnt = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j])
        for k in range(4):
            if board[i][j] <= board[i+dx[k]][j+dy[k]]:
                break
        else:
            cnt += 1

print(cnt)
