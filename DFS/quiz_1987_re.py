# 성공! (재도전)
# 풀이시간: 15분
# 이전 코드와 다른 점: 말이 지나온 알파벳을 체크하는 로직이 다름.
# 메모: 백준으로 채점시 언어를 PyPy3로 지정해야함. (Python3로 채점시 시간초과 발생.)

import sys
sys.stdin = open("input.txt")

# 상, 하, 좌, 우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def DFS(y, x, cnt):
    global result
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            ordinal = ord(board[ny][nx]) - ord('A')
            if visited[ordinal] == 0:
                visited[ordinal] = 1
                DFS(ny, nx, cnt+1)
                visited[ordinal] = 0
    if result < cnt:
        result = cnt


# 세로, 가로
r, c = map(int, input().split())
board = []
for _ in range(r):
    row = list(input())
    board.append(row)

visited = [0] * 26 # 말이 지나온 알파벳을 기록하는 리스트
result = 0


visited[ord(board[0][0]) - ord('A')] = 1 # 1행 1열(시작점)의 알파벳은 방문했다고 체크
DFS(0, 0, 1)

print(result)

