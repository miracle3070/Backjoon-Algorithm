# 실패!
# 풀이시간: 15분


INF = int(1e9)

n = int(input())
memory = [INF] * (n+1)
memory[0] = 0
memory[1] = 0

for i in range(1, n//3 + 1):
    calc = i * 3
    if memory[i] != INF and (memory[i] + 1) < memory[calc]:
        memory[calc] = memory[i] + 1

for i in range(1, n//2 + 1):
    calc = i * 2
    if memory[i] != INF and (memory[i] + 1) < memory[calc]:
        memory[calc] = memory[i] + 1

for i in range(1, n):
    calc = i + 1
    if memory[i] != INF and (memory[i] + 1) < memory[calc]:
        memory[calc] = memory[i] + 1

print(memory[n])