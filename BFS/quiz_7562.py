# 성공
# 풀이시간: 13분

from collections import deque
import sys
sys.stdin = open("input.txt", "r")

dy = (-2, -1, 1, 2, 2, 1, -1, -2)
dx = (-1, -2, -2, -1, 1, 2, 2, 1)

def BFS(start):
    queue = deque([start])
    y, x = start
    board[y][x] = 1

    while queue:
        y, x = queue.popleft()
        if y == end[0] and x == end[1]:
            result = board[y][x]
            return result
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] == 0:
                    board[ny][nx] = board[y][x] + 1
                    queue.append((ny, nx))

# 테스트 케이스 개수
case = int(input())
for _ in range(case):
    # 체스판 한 변의 길이
    n = int(input())
    board = [[0] * n for _ in range(n)]

    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    result = BFS(start)
    print(result - 1)