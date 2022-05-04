# 성공!
# 풀이시간: 5분


import sys
sys.stdin = open("input.txt", "r")


t = int(input())
for _ in range(t):
    p = ""
    r, s = input().split()
    r = int(r)
    for c in s:
        p += c*r
    print(p)