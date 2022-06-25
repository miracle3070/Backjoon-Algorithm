# 성공
# 풀이시간: 20분
# 메모: 이건 절대 실버5 문제가 아닌데?

import sys
sys.stdin = open("input.txt", "r")

sys.setrecursionlimit(int(1e9))

# 아래, 오른쪽
dy = (1, 0)
dx = (0, 1)

def DFS(y, x, cnt):
    global result
    if result:
        return
    if board[y][x] == -1:
        result = True
        return
    for i in range(2):
        ny = y + dy[i] * cnt
        nx = x + dx[i] * cnt
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            visited[ny][nx] = 1
            DFS(ny, nx, board[ny][nx])
            visited[ny][nx] = 0

n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1
c = board[0][0]
result = False
DFS(0, 0, c)

if result:
    print("HaruHaru")
else:
    print("Hing")