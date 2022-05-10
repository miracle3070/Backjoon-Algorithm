# 성공
# 풀이시간: 13분
# 메모: 문자열 처리 부분이 쉽지 않았음.

import sys
sys.stdin = open("input.txt", "r")

# 단어의 개수
n = int(input())
result = 0
for _ in range(n):
    word = input()
    dic = dict()
    for w in set(word):
        dic[w] = word.count(w)
    for ch, cnt in dic.items():
        temp = word.replace(ch * cnt, "")
        if temp == word:
            break
    else:
        result += 1
print(result)