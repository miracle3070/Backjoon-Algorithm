# 성공
# 풀이시간: 4분


import sys
sys.stdin = open("input.txt", "r")


n = int(input())
result = 1

for x in range(1, n+1):
    result *= x

print(result)