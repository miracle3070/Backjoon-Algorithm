# 실패!
# 풀이시간: 34분
# 메모: 1. 문제 조건을 잘못읽어서 오래걸림. / 2. 지금 풀이는 메모리 초과 판정이 나옴. 향후 수정 필요.

import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(int(1e9))

# 상, 하, 좌, 우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1 ,1)


def DFS(y, x, count):
    global result
    memory[count] = board[y][x]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if board[ny][nx] not in memory:
                DFS(ny, nx, count+1)
    memory[count] = 0
    if result < count:
        result = count

# 세로, 가로 길이
r, c = map(int, input().split())

board = []
for _ in range(r):
    row = list(input())
    board.append(row)

memory = [0] * (r * c + 1)
result = 0
DFS(0, 0, 0)

print(result+1) # 시작점도 횟수에 포함