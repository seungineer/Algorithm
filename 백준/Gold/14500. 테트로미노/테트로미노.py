import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
max_score = -1
vis = [[-1 for _ in range(m)]for _ in range(n)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def t(i, j, score, l):
    if i < 0 or n <= i or j < 0 or m <= j:
            return
    global max_score
    if l == 0 or l == 1: # 하 or 상
        if j < 1 or m-1 <= j:
            return
        score += matrix[i][j]
        score += matrix[i][j-1]
        score += matrix[i][j+1]
        max_score = max(max_score, score)
    elif l == 2 or l == 3: # 우 or 좌
        if i < 1 or n-1 <= i:
            return
        score += matrix[i][j]
        score += matrix[i+1][j]
        score += matrix[i-1][j]
        max_score = max(max_score, score)
vis_lst = []
def dfs(i, j, depth, score):
    global max_score
    score += matrix[i][j]
    # vis[i][j] = 1
    vis_lst.append([i, j])
    if depth == 4:
        max_score = max(max_score, score)
        # vis[i][j] = -1
        return
    if depth == 1:
        # T 모양 처리
        for l in range(4):
            t(i+di[l], j+dj[l], score, l)
    for k in range(4):
        if i+di[k] < 0 or i+di[k] >= n or j+dj[k] < 0 or j+dj[k] >= m:
            continue
        if [i+di[k], j+dj[k]] in vis_lst:
            continue 
        dfs(i+di[k], j+dj[k], depth+1, score)
        vis_lst.remove([i+di[k], j+dj[k]])
        

for i in range(n):
    for j in range(m):
        dfs(i, j, 1, 0)
        vis_lst = []

print(max_score)