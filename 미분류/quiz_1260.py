from collections import deque


def DFS(v):
    visited[v] = True
    print(v, end=" ")
    for x in graph[v]:
        if visited[x] == False:
            DFS(x)


def BFS(v):
    q = deque([v])
    visited[v] = True
    while q:
        out = q.popleft()
        print(out, end=" ")
        for x in graph[out]:
            if visited[x] == False:
                visited[x] = True
                q.append(x)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

DFS(v)
print()

visited = [False] * (n+1)
BFS(v)
