# 성공
# 풀이시간: 34분
# 메모: 점화식을 떠올리는게 힘들었음. (다이나믹으로 작성할 식이 떠오르지 않음.)

import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for _ in range(t):
    n = int(input())
    memory = [0] * (n+1+3)
    memory[1] = 1
    memory[2] = 2
    memory[3] = 4
    for i in range(4, n+1):
        memory[i] = memory[i-1] + memory[i-2] + memory[i-3]
    print(memory[n])