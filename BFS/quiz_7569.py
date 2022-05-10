# 성공
# 풀이시간: 70분
# 오래걸린 이유 1: 3차원 리스트를 다루는데 익숙하지 않아서 실수가 많았음.
# 오래걸린 이유 2: 변수 x를 z로 잘못적는 바람에 삽질을 오래함.

from collections import deque
import sys
sys.stdin = open("input.txt", "r")

# 상, 하, 좌, 우, 앞, 뒤
dy = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)


def BFS():
    queue = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if boxes[z][y][x] == 1:
                    queue.append((z, y, x))

    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if boxes[nz][ny][nx] == 0:
                    boxes[nz][ny][nx] = boxes[z][y][x] + 1
                    queue.append((nz, ny, nx))

# 가로, 세로, 높이
m, n, h = map(int, input().split())

boxes = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        row = list(map(int, input().split()))
        boxes[i].append(row)

BFS()

result = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if boxes[z][y][x] == 0:
                print(-1)
                sys.exit(0)
            if result < boxes[z][y][x]:
                result = boxes[z][y][x]

print(result-1) # 이미 익었던 토마토는 일수에서 뺀다.