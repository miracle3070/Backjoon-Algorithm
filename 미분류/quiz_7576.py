from collections import deque
import sys
sys.stdin = open("input.txt")


# 왼쪽, 오른쪽, 위, 아래
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def BFS():
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 0:
                    board[ny][nx] = board[y][x] + 1
                    q.append((ny, nx))


m, n = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

q = deque()
for i in range(n): # 세로
    for k in range(m): # 가로
        if board[i][k] == 1:
            q.append((i, k))

BFS()

max_value = -1
for i in range(n):
    for k in range(m):
        if board[i][k] == 0:
            print(-1)
            sys.exit(0)
        else:
            if max_value < board[i][k]:
                max_value = board[i][k]

print(max_value-1)
