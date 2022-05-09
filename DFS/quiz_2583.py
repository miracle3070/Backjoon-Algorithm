# 성공
# 풀이시간: 28분
# 오래 걸린 이유: DFS 진행할 때 시작위치도 방문처리하는 것을 깜빡하고 삽질함.

import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(int(1e9))

# 상, 하, 좌, 우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def DFS(y, x):
    global single_area
    board[y][x] = 1
    single_area += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n:
            if board[ny][nx] == 0:
                DFS(ny, nx)


# 세로, 가로, 직사각형 개수
m, n, k = map(int, input().split())

# 직사각형 영역 색칠
board = [[0] * n for _ in range(m)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly, ry):
        for x in range(lx, rx):
            board[y][x] = 1

area = []
cnt = 0
for y in range(m):
    for x in range(n):
        if board[y][x] == 0:
            single_area = 0
            cnt += 1
            DFS(y, x)
            area.append(single_area)
area.sort()

# 최종결과 출력
print(cnt)
for a in area:
    print(a, end=" ")