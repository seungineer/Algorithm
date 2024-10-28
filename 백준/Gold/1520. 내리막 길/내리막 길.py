from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)]for _ in range(N)]

def check(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    isAlloc = True
    allocNum = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if matrix[x][y] < matrix[nx][ny]:
                if dp[nx][ny] == -1:
                    isAlloc = False
                else:
                    allocNum += dp[nx][ny]

    if isAlloc: dp[x][y] = allocNum

        
dp[0][0] = 1
num = 0
cnt = 0

lst = deque()
for i in range(N*M): lst.append(i)

while lst:
    num = lst.popleft()
    i = (num // M) % N
    j = num % M
    if dp[i][j] == -1:
        check(i,j)
        if dp[i][j] == -1:
            lst.append(num)

print(dp[-1][-1])
