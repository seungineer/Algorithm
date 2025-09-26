from collections import deque

def bfs(matrix, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    qu = deque()
    vis = [[0 for _ in range(m)] for _ in range(n)]
    qu.append([0, 0, 1])
    vis[0][0] = 1
    while qu:
        x, y, dis = qu.popleft()
        if x == n-1 and y == m-1:
            return dis
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if vis[nx][ny] == 0 and matrix[nx][ny] == 1:
                    vis[nx][ny] = 1
                    qu.append([nx, ny, dis + 1])
    return -1
    

def solution(maps):
    return bfs(maps, len(maps), len(maps[0]))