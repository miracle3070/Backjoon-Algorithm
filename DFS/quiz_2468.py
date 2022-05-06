# 성공
# 풀이시간: 50분
# 오래 걸린 이유: 수면의 높이가 0인 경우를 생각하지 못함.

import sys, copy
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(int(1e9))

# 상, 하, 좌, 우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def DFS(b, y, x, h):
    b[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if b[ny][nx] > h:
                DFS(b, ny, nx, h)

n = int(input())
board = []
max_h = 0
for _ in range(n):
    row = list(map(int, input().split()))
    row_max = max(row)
    if max_h < row_max:
        max_h = row_max
    board.append(row)

result = 0
for h in range(0, max_h):
    cnt = 0
    b = copy.deepcopy(board)
    for y in range(n):
        for x in range(n):
            if b[y][x] > h:
                DFS(b, y, x, h)
                cnt += 1
    if result < cnt:
        result = cnt
print(result)

