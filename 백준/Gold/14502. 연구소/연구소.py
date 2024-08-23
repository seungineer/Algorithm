import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < m and vis[nx][ny] == False :
            if matrix[nx][ny] == 0:
                vis[nx][ny] = True
                dfs(nx, ny)

def zero_cnt(matrix, vis):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0 and vis[i][j] == False:
                cnt += 1
    return cnt



def find_area(matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2 and vis[i][j] == False:
                vis[i][j] = True
                dfs(i,j) #전염 가능 구역 vis 표시 -> 추후 vis false and matrix 0인 개수 카운트
    
    return zero_cnt(matrix, vis)

# 벽 세 개 넣기
max_area = -float("inf")
vis = [[False for _ in range(m)] for _ in range(n)]
for a in range(n*m):
    x1 = a // m
    y1 = a % m
    for b in range(a+1, n*m):
        x2 = b // m
        y2 = b % m
        for c in range(b+1, n*m):
            x3 = c // m
            y3 = c % m
            if matrix[x1][y1] == 0 and matrix[x2][y2] == 0 and matrix[x3][y3] == 0:
                matrix[x1][y1] = 1
                matrix[x2][y2] = 1
                matrix[x3][y3] = 1
                max_area = max(max_area, find_area(matrix))
                matrix[x1][y1] = 0
                matrix[x2][y2] = 0
                matrix[x3][y3] = 0
                vis = [[False for _ in range(m)] for _ in range(n)]
            else:
                continue

print(max_area)