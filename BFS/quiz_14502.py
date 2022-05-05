# 성공
# 풀이시간: 1시간 30분
# 벽을 세팅(1을 세팅)하는 코드를 구현하는 과정에서 오래걸렸음.

import sys
import copy
from collections import deque
sys.stdin = open("input.txt", "r")

# 상, 하, 좌, 우
dx = (0, 0, -1, 1)  # 가로 이동
dy = (-1, 1, 0, 0)  # 세로 이동

def BFS(g):
    global result
    graph = copy.deepcopy(g)
    q = deque()
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 2:
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 2
                    q.append((ny, nx))
    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                cnt += 1
    result = max(result, cnt)

# 세로, 가로
n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


result = 0
for a in range(n):
    for b in range(m):
        if graph[a][b] != 0:
            continue
        graph[a][b] = 1
        for c in range(a, n):
            for d in range(m):
                if graph[c][d] != 0 or (c == a and d < b):
                    continue
                graph[c][d] = 1
                for e in range(c, n):
                    for f in range(m):
                        if graph[e][f] != 0 or (e == c and f < d):
                            continue
                        graph[e][f] = 1
                        BFS(graph)
                        graph[e][f] = 0
                graph[c][d] = 0
        graph[a][b] = 0
print(result)



