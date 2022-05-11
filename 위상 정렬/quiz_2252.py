# 성공
# 풀이시간: 12분
# 메모: 위상 정렬 알고리즘에 익숙하지 않아서 오래걸림.

from collections import deque
import sys
sys.stdin = open("input.txt", "r")

# 위상 정렬
def topology_sort():
    q = deque()
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((0, i))
    while q:
        ind, now = q.popleft()
        result.append(now)
        for linked in graph[now]:
            indegree[linked] -= 1
            if indegree[linked] == 0:
                q.append((0, linked))
    return result


# 학생 수, 키를 비교한 횟수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1) # 진입차수

# 키를 비교한 내역
for _ in range(m):
    a, b = map(int, input().split()) # a가 b앞에 선다
    graph[a].append(b)
    indegree[b] += 1

result = topology_sort()
for r in result:
    print(r, end=" ")
