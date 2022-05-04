# 성공!
# 풀이시간: 10분

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def BFS(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visited[n] == False:
                queue.append(n)
                visited[n] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        BFS(i)
        cnt += 1

print(cnt)