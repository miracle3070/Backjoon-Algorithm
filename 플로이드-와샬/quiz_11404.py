# 성공!
# 풀이시간: 10분
# 메모: 백준으로 채점시 언어를 PyPy3로 선택해야함. (Python3은 채점 속도가 너무 느림.)

import sys
#sys.stdin = open("input.txt", "r")
INF = int(1e9)


# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

# 버스(간선) 정보
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 자기자신으로 가는 경로는 0
for i in range(1, n+1):
    graph[i][i] = 0

# 플로이드-와샬 알고리즘 진행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 최종결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if 0 < graph[a][b] <INF:
            print(graph[a][b], end=" ")
        else:
            print(0, end=" ")
    print()