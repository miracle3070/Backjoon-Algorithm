# 성공
# 풀이시간: 10분

import sys
sys.stdin = open("input.txt", "r")
INF = int(1e9)

n = int(input())
memory = [INF] * (n+1)
memory[n] = 0

for i in range(n, 0, -1):
    cnt = memory[i] + 1
    if i % 3 == 0:
        t = i // 3
        memory[t] = min(memory[t], cnt)
    if i % 2 == 0:
        t = i // 2
        memory[t] = min(memory[t], cnt)
    t = i - 1
    memory[t] = min(memory[t], cnt)

print(memory[1])