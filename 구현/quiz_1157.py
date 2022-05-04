# 성공!
# 풀이시간: 9분
import sys
sys.stdin = open("input.txt", "r")


cnt = [0] * 26
string = input().upper()

for s in string:
    idx = ord(s) - ord('A')
    cnt[idx] += 1

max_value = -1
max_idx = -1
for i in range(len(cnt)):
    if max_value < cnt[i]:
        max_value = cnt[i]
        max_idx = i

if cnt.count(max_value) == 1:
    print(chr(max_idx + ord('A')))
else:
    print('?')