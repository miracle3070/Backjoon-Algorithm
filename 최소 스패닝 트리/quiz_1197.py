# 성공
# 풀이시간: 10분
# 메모: 크루스칼 알고리즘 공부한지 얼마 안돼서 금방 해결. 추후 다시 도전해볼것.

import sys
sys.stdin = open("input.txt", "r")

# 부모(루트) 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합집합 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 정점의 개수, 간선의 개수
v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# 간선 정보 입력
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)