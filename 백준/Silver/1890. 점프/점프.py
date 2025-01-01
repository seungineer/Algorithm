from collections import deque
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

qu = deque()
qu.append([0,0])
cand = [[0 for _ in range(N)] for _ in range(N)]
while qu:
    x, y = qu.popleft()
    if cand[x][y] == 0:
        cand[x][y] = 1
        jump = matrix[x][y]
        diff = [[jump, 0], [0, jump]]
        for delta in diff:
            dx, dy = delta
            nx = x + dx
            ny = y + dy
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if cand[nx][ny] == 0:
                    qu.append([nx, ny])

cand[-1][-1] = 0
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if cand[i][j] == 0: continue
        jump = matrix[i][j]
        diff = [[jump, 0], [0, jump]]
        for delta in diff:
            dx, dy = delta
            nx = i + dx
            ny = j + dy
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                dp[nx][ny] += dp[i][j]

print(dp[-1][-1])
