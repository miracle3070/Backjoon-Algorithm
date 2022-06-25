# 성공
# 풀이시간: 11분

import sys
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
nums = [1] * (n+1)
cnt = 0
result = 0

for i in range(2, n+1):
    if nums[i]:
        nums[i] = 0
        cnt += 1
        if cnt == k:
            result = i
            break
        for j in range(2, n+1):
            if i * j > n:
                break
            if nums[i * j]:
                nums[i * j] = 0
                cnt += 1
                if cnt == k:
                    result = i * j
                    break
    if cnt == k:
        break

print(result)