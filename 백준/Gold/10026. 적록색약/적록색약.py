import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

area_cnt = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
matrix_check = [[False]*n for _ in range(n)]

def dfs_normal(i, j, color):
    
    if color == matrix[i][j]:
        matrix_check[i][j] = True

        for idx in range(4):
            ni = i + dy[idx]
            nj = j + dx[idx]
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            if matrix_check[ni][nj] == True:
                continue
            dfs_normal(ni, nj, color)

# normal count
for i in range(n):
    for j in range(n):
        if matrix_check[i][j] != 1:
            area_cnt += 1
            color = matrix[i][j]
            dfs_normal(i, j, color)
print(area_cnt, end=' ')

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

# abnormal count
matrix_check = [[False]*n for _ in range(n)]
area_cnt = 0
for i in range(n):
    for j in range(n):
        if matrix_check[i][j] != True:
            area_cnt += 1
            color = matrix[i][j]
            dfs_normal(i, j, color)

print(area_cnt)
