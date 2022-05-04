# 실패
import sys
sys.stdin = open("input.txt", "r")


def DFS(start, target):
    graph[start][target] = 0
    graph[target][start] = 0
    for x in graph[target]:
        if graph[target][x] == 1:
            DFS(target, x)


n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for x in graph:
    print(x)

cnt = 0

for i in range(1, n+1):
    for k in range(1, n+1):
        if graph[i][k] == 1:
            print(i, k)
            DFS(i, k)
            cnt += 1

print(cnt)