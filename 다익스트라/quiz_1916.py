# 성공!
# 풀이시간: 10분
# 메모: 백준에서 채점시 언어를 PyPy3로 설정해야함. (Python3 선택시 시간초과 나옴.)


import sys, heapq
sys.stdin = open("input.txt", "r")
INF = int(1e9)

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

# 버스(간선) 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발지, 도착지 입력받기
start, end = map(int, input().split())

# 최단거리 테이블 초기화
distance = [INF] * (n+1)


# 다익스트라 정의
def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start))
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
dijkstra(start)

# 결과 출력
print(distance[end])