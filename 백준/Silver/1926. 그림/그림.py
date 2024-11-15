import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if matrix[nx][ny] == 1:
                cnt[0] += 1
                matrix[nx][ny] = 0
                dfs(nx, ny)
    return

cnt_pic = 0
max_cnt = [0]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            cnt = [1]
            matrix[i][j] = 0
            dfs(i, j)
            max_cnt[0] = max(max_cnt[0], cnt[0])
            cnt_pic += 1
print(cnt_pic)
print(max_cnt[0])