# 성공!
# 풀이시간: 14분

#import sys
#sys.stdin = open("input.txt", "r")


n = int(input())
memory = [-1] * (n+1)
memory[0] = 0

for weight in (3, 5):
    for i in range(weight, n+1):
        result = -1
        if memory[i-weight] == -1:
            continue
        else:
            result = memory[i-weight] + 1
            if memory[i] == -1:
                memory[i] = result
            else:
                memory[i] = min(memory[i], result)

print(memory[n])
