# 성공
# 풀이시간: 24분

import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)

# 정점의 개수
n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for a in range(n):
    for b in range(n):
        if a != b and graph[a][b] == 0:
            graph[a][b] = INF

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a != b:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            else:
                if graph[a][b] == 0 and 0 < graph[a][k] + graph[k][b] < INF:
                    graph[a][b] = graph[a][k] + graph[k][b]


for a in range(n):
    for b in range(n):
        if 0 < graph[a][b] < INF:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()