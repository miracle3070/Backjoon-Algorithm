# 성공!
# 풀이시간: 13분

import sys
sys.stdin = open("input.txt", "r")

from collections import deque
# 뒤로, 앞으로
SIZE = 100_000
dx = (-1, 1)
INF = int(1e9)


def BFS(n, k):
    memory[n] = 0
    queue = deque([n])
    while queue:
        x = queue.popleft()
        for i in range(3):
            if i < 2:
                nx = x + dx[i]
            else:
                nx = x * 2
            if 0 <= nx <= SIZE and memory[nx] == INF:
                memory[nx] = memory[x] + 1
                queue.append(nx)
                if nx == k:
                    return


n, k = map(int, input().split())
memory = [INF] * (SIZE+1)
BFS(n, k)
print(memory[k])