# 실패
# 풀이시간: 32분
# 메모: 예제에서는 올바르게 동작하나 채점하면 틀렸다고 나옴. 추후 반례에 대해 확인할 것.

from collections import deque
import sys
sys.stdin = open("input.txt", "r")


# 위상 정렬
def topology_sort(target):
    result = 0
    q = deque()
    spend = 0
    node_list = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            node_list.append(i)
            spend = max(spend, time[i])
    result += spend
    if node_list:
        q.append(node_list)

    while q:
        spend = 0
        tmp = []
        node_list = q.popleft()
        if target in node_list:
            break
        for node in node_list:
            for linked in graph[node]:
                spend = max(spend, time[linked])
                indegree[linked] -= 1
                if indegree[linked] == 0:
                    tmp.append(linked)
        result += spend
        if tmp:
            q.append(tmp)
    return result


# 테스트케이스 개수
t = int(input())

for _ in range(t):
    # 건물의 개수, 건물간 건설 규칙의 총 개수
    n, k = map(int,input().split())

    time = list(map(int, input().split()))
    time.insert(0, 0)
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    result = topology_sort(w)
    print(result)