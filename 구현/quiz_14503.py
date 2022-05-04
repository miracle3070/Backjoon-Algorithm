# 성공!
# 풀이시간: 36분

import sys
sys.stdin = open("input.txt", "r")

# 북, 동, 남, 서
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)


n, m = map(int, input().split())
y, x, d = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

cnt = 0
while True:
    if board[y][x] == 0:
        board[y][x] = 2
        cnt += 1
    for i in range(1, 5):
        nx = x + dx[(d - i) % 4]
        ny = y + dy[(d - i) % 4]
        if board[ny][nx] == 0:
            d = (d - i) % 4
            x = nx
            y = ny
            break
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if board[ny][nx] == 1:
            break
        else:
            x = nx
            y = ny
print(cnt)
