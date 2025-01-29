from collections import deque
import sys
input = sys.stdin.readline
def solution():
    L, R, C = map(int, input().rstrip().split())
    if L == 0: exit() # 종료 조건

    matrix = []
    for l in range(L):
        matrix.append([])
        for r in range(R):
            matrix[-1].append(list(map(str, input().rstrip())))
        input() # 구분선 처리

    def inRange(x, y, z):
        if 0 <= x and x < R and 0 <= y and y < C and 0 <= z and z < L:
            return True
        return False

    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    qu = deque()
    for k in range(L):
        for i in range(R):
            for j in range(C):
                if matrix[k][i][j] == 'S': ST_X, ST_Y, ST_Z = i, j, k
    vis = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    qu.append((ST_X, ST_Y, ST_Z, 0)) # (시작지점, 걸린 시간)
    vis[ST_Z][ST_X][ST_Y] = 1
    ans = -1
    while qu:
        x, y, z, time = qu.popleft()
        for a in range(6):
            nx = x + dx[a]
            ny = y + dy[a]
            nz = z + dz[a]
            if inRange(nx, ny, nz):
                if vis[nz][nx][ny] == 0 and matrix[nz][nx][ny] == '.':
                    vis[nz][nx][ny] = 1
                    qu.append((nx, ny, nz, time + 1))
                if vis[nz][nx][ny] == 0 and matrix[nz][nx][ny] == 'E':
                    vis[nz][nx][ny] = 1
                    ans = time + 1
            if ans != -1: break
        if ans != -1: break

    if ans != -1:
        print(f"Escaped in {ans} minute(s).")
    else:
        print("Trapped!")

while True:
    solution()
