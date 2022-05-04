# 성공!
# 풀이시간: 20분
# DFS를 반복문으로 고치려면 어떻게 해야할까?

import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(int(1e9))

# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = (0, 0, -1, 1, -1, -1, 1, 1)
dy = (-1, 1, 0, 0, -1, 1, -1, 1)


def DFS(y, x):
    board[y][x] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if board[ny][nx] == 1:
                DFS(ny, nx)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    board = []
    for _ in range(h):
        row = list(map(int, input().split()))
        board.append(row)

    for i in range(h):
        for k in range(w):
            if board[i][k] == 1:
                DFS(i, k)
                cnt += 1
    print(cnt)

