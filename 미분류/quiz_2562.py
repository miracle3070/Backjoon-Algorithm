# 성공!
# 풀이시간: 4분

import sys
sys.stdin = open("input.txt","r")


max_value = -1
idx = -1

for i in range(9):
    num = int(input())
    if max_value < num:
        max_value = num
        idx = i

print(max_value)
print(idx+1)