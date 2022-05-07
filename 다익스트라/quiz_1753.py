# 성공
# 풀이시간: 13분
# 백준 채점시 언어를 PyPy3로 설정해야함. (Python3로 설정하면 시간초과 나옴.)

import sys, heapq
sys.stdin = open("input.txt", "r")
INF = int(1e9)


# 정점의 개수, 간선의 수
v, e = map(int, input().split())
# 시작 정점의 번호
k = int(input())

graph = [[] for _ in range(v+1)] # 그래프 정의
distance = [INF] * (v+1) # 최단거리 테이블

# 간서 입력받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # (목적지, 거리)


# 다익스트라 정의
def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start)) # (거리, 노드번호)
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for linked in graph[now]:
            cost = dist + linked[1]
            if cost < distance[linked[0]]:
                distance[linked[0]] = cost
                heapq.heappush(h, (cost, linked[0]))

# 다익스트라 호출
dijkstra(k)

for i in range(1, v+1):
    if distance[i] < INF:
        print(distance[i])
    else:
        print("INF")