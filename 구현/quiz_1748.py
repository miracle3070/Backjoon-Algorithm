# 성공
# 풀이시간: 31분
# 메모: 1. 문제해결을 위한 공식을 떠올리는게 힘들었음. / 2. 공식을 코드로 구현하는 것도 힘들었음.

import sys
sys.stdin = open("input.txt", "r")

n = input()
length = len(n)
num = int(n)

result = 0
m = num // (10 ** (length-1)) # 가장 큰 자리수의 숫자

if length < 2:
    result = num
else:
    result += 9
    for i in range(1, length-1):
        t = (10 ** i) * 9 * (i + 1)
        result += t
    t = (10 ** (length-1)) * (m-1) * length
    result += t
    result += ((num % (m * (10 ** (length-1)))) + 1) * length

print(result)