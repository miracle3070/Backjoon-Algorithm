# 성공
# 풀이시간: 15분

from collections import deque
import sys, copy
sys.stdin = open("input.txt", "r")


# 상, 하, 좌, 우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


# BFS 정의
def BFS(y, x):
    target = b[y][x]
    b[y][x] = 'C'
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if b[ny][nx] == target:
                    b[ny][nx] = 'C'
                    queue.append((ny, nx))

n = int(input())
board = []
for _ in range(n):
    row = list(input())
    board.append(row)

cnt = 0
cnt_weakness = 0

# 일반
b = copy.deepcopy(board)
for y in range(n):
    for x in range(n):
        if b[y][x] != 'C':
            BFS(y, x)
            cnt += 1

# 적록색약
b = copy.deepcopy(board)
for y in range(n):
    for x in range(n):
        if b[y][x] == 'G':
            b[y][x] = 'R' # 초록색을 빨간색으로 모두 바꾼다. (구분을 못하기 때문)

for y in range(n):
    for x in range(n):
        if b[y][x] != 'C':
            BFS(y, x)
            cnt_weakness += 1


# 최종결과 출력
print(cnt, cnt_weakness)