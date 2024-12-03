from collections import deque
M, N = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

def bfs(x, y):
    queue = deque()
    vis[x][y] = 1
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1: isFind[0] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if vis[nx][ny] == 0 and matrix[nx][ny] == 0:
                    vis[nx][ny] = 1
                    queue.append([nx, ny])

isFind = [False]
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]
ans = 0
while True:
    vis = [[0 for _ in range(M)] for _ in range(N)]
    bfs(0 ,0)
    if isFind[0]: break
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx and nx < N and 0 <= ny and ny < M:
                        if vis[nx][ny] == 1:
                            matrix[i][j] = 0
    ans += 1
print(ans)
