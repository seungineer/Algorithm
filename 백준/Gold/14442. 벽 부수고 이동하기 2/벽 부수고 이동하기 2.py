from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())
    matrix = [list(map(str, input().rstrip())) for _ in range(N)]
    ST_X, ST_Y, EN_X, EN_Y = 0, 0, N-1, M-1
    minDistance = -1
    vis = [[[int(1e9) for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    qu = deque()
    qu.append((ST_X, ST_Y, 0, 1)) # 위치, 부순 횟수, 거리
    vis[ST_X][ST_Y][0] = 1
    while qu:
        x, y, broken, distance = qu.popleft()
        if x == EN_X and y == EN_Y:
            minDistance = distance
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == '0':
                    if distance + 1 < vis[nx][ny][broken]:
                        vis[nx][ny][broken] = distance + 1
                        qu.append((nx, ny, broken, distance+1))
                else:
                    if broken >= K: continue
                    if distance + 1 < vis[nx][ny][broken+1]:
                        vis[nx][ny][broken+1] = distance + 1
                        qu.append((nx, ny, broken+1, distance+1))
    
    print(minDistance)

solution()