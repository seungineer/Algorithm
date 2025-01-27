import sys
from collections import deque
input = sys.stdin.readline
def solution():
    K = int(input())
    M, N = map(int, input().rstrip().split())
    matrix = list(list(map(int, input().rstrip().split())) for _ in range(N))
    
    ST_X, ST_Y = 0, 0
    EN_X, EN_Y = N-1, M-1
    vis = [[[int(1e5) for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    dx_j = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy_j = [-2, -1, 1, 2, 2, 1, -1, -2]
    
    qu = deque()
    qu.append((ST_X, ST_Y, 0, 0)) # (x, y, 점프 횟수, 걸린 시간)
    
    while qu:
        x, y, jump, time = qu.popleft()
        if vis[x][y][jump] < time: continue
        vis[x][y][jump] = min(vis[x][y][jump], time)
        # 인접한 위치로 이동
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if matrix[nx][ny] == 1: continue
                if vis[nx][ny][jump] <= time + 1: continue
                vis[nx][ny][jump] = time + 1
                qu.append((nx, ny, jump, time+1))
        # 점프해서 이동
        for k in range(8):
            nx = x + dx_j[k]
            ny = y + dy_j[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if matrix[nx][ny] == 1: continue
                if jump + 1 > K: continue
                if vis[nx][ny][jump+1] <= time + 1: continue
                vis[nx][ny][jump+1] = time + 1
                qu.append((nx, ny, jump+1, time+1))
    
    if min(vis[-1][-1]) == int(1e5): print(-1)
    else: print(min(vis[-1][-1]))
solution()