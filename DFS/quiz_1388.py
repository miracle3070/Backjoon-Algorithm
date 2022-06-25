# 성공
# 풀이시간: 12분

import sys
sys.stdin = open("input.txt", "r")

dy = (-1, 1)
dx = (-1, 1)

def DFS_row(y, x):
    for i in range(2):
        nx = x + dx[i]
        if 0 <= nx < m and board[y][nx] == '-':
            board[y][nx] = '.'
            DFS_row(y, nx)

def DFS_col(y, x):
    for i in range(2):
        ny = y + dy[i]
        if 0 <= ny < n and board[ny][x] == '|':
            board[ny][x] = '.'
            DFS_col(ny, x)


n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(input())
    board.append(row)

cnt = 0
for i in range(n):
    for k in range(m):
        if board[i][k] == '-':
            board[i][k] = '.'
            DFS_row(i, k)
            cnt += 1
        elif board[i][k] == '|':
            DFS_col(i, k)
            cnt += 1
        else:
            pass

print(cnt)