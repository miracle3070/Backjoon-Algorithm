# 실패작
import sys
sys.stdin = open("input.txt", "r")


def DFS(end):
    global cnt
    if visited[end] == 1 or graph[end] == []:
        cnt += 1
        return
    else:
        visited[end] = 1
        for x in graph[end]:
            if visited[x] == 0:
                print(x)
                DFS(x)





n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visited = [0] * (n+1)
DFS(1)

print(cnt)
