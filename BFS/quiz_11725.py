# 실패
# 풀이시간: 22분
# 메모: 문제 입출력 예제를 이해하지 못함. / 트리 문제에 많이 취약

import sys
sys.stdin = open("input.txt", "t")

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)

for target in range(1, n+1):
    parent = -1
    DFS(target)
    print(target)