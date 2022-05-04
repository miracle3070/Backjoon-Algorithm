# 성공!
# 풀이시간: 8분

import sys
sys.stdin = open("input.txt", "r")


result = [-1] * 26

string = input()
for i in range(len(string)):
    c = string[i]
    idx = ord(c) - ord('a')
    if result[idx] == -1:
        result[idx] = i

for x in result:
    print(x, end=" ")

