import sys
input = sys.stdin.readline
N, M = map(int, input().split())
R, C, D = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
vis = [[0 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isInbound(r, c):
    if 0 <= r and r < N:
        if 0 <= c and c < M:
            return True
    else:
        return False

def isAllVis(r, c):
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if isInbound(nr, nc):
            # 벽이 아니면서 방문하지 않은 경우 False
            if matrix[nr][nc] == 0 and vis[nr][nc] == 0:
                return False
    return True
dirR = [-1, 0, 1, 0]
dirC = [0, 1, 0, -1]

def canGoBack(R,C,D):
    # D 0 북 1 동 2 남 3 서
    
    nr = R - dirR[D]
    nc = C - dirC[D]
    if isInbound(nr, nc):
        if matrix[nr][nc] == 0:
            return nr, nc, D, True
        else:
            return R, C, D, False

answer = 0
while True:
    if vis[R][C] == 0:
        vis[R][C] = answer + 1
        answer += 1

    if isAllVis(R, C):
        R, C, D, isGoBack = canGoBack(R, C, D)
        if isGoBack:
            continue
        else:
            print(answer)
            exit()
    else:
        D -= 1
        if D < 0 : D = 3
        
        nr = R + dirR[D]
        nc = C + dirC[D]
        if matrix[nr][nc] == 0 and vis[nr][nc] == 0:
            R, C = nr, nc