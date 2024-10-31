import sys, copy
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def calResolve(i, j):
    dx = [1, -1, 0, 0]
    dy = [0 ,0 ,1, -1]
    resolving = 0
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni and ni < N and 0 <= nj and nj < M:
            if matrix[ni][nj] == 0: resolving += 1
    new_matrix[i][j] -= resolving
    if new_matrix[i][j] < 0: new_matrix[i][j] = 0
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni and ni < N and 0 <= nj and nj < M:
            if matrix[ni][nj] != 0 and vis[ni][nj] == 0:
                vis[ni][nj] = 1
                calResolve(ni, nj)


def dfs(i, j):
    dx = [1, -1, 0, 0]
    dy = [0 ,0 ,1, -1]
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni and ni < N and 0 <= nj and nj < M:
            if matrix[ni][nj] != 0 and vis[ni][nj] == 0:
                vis[ni][nj] = 1
                dfs(ni, nj)

answer = 0
isFind = False
while True:
    cnt = 0
    isDone = True
    vis = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if  matrix[i][j] != 0 and vis[i][j] == 0:
                isDone = False
                cnt += 1
                vis[i][j] = 1
                dfs(i, j)
    
    if cnt >= 2:
        isFind = True
        break
    if isDone: break
    answer += 1
    vis = [[0 for _ in range(M)] for _ in range(N)]
    new_matrix = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0 and vis[i][j] == 0:
                vis[i][j] = 1
                calResolve(i, j)
    matrix = copy.deepcopy(new_matrix)
    # 대륙 개수 세기
if isFind: print(answer)
else: print(0)
# 2개 이상이면 끝내기