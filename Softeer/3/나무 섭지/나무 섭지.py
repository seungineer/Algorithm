import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
matrix = [list(map(str, input().strip())) for _ in range(N)]

ghosts = []
namwoos = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'G': ghosts.append([i, j])
        if matrix[i][j] == 'N': namwoos.append([i, j])
        if matrix[i][j] == 'D': exit_x, exit_y = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
    vis = [[0 for _ in range(M)] for _ in range(N)]
    
    def mark_ghost(x, y):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if vis[nx][ny] == 0 or vis[nx][ny] == 1:
                    if matrix[nx][ny] != 'G':
                        vis[nx][ny] = 2
                        matrix[nx][ny] = 'G'
                        additional_ghosts.add((nx, ny))
    
    def mark_namwoo(x, y):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if vis[nx][ny] == 0:
                    if (matrix[nx][ny] == '.' or matrix[nx][ny] == 'D'):
                        vis[nx][ny] = 1
                        matrix[nx][ny] = 'N'
                        additional_namwoo.add((nx, ny))
                        
    additional_namwoo = set()
    for namwoo in namwoos:
        n_x, n_y = namwoo
        vis[n_x][n_y] = 1
        mark_namwoo(n_x, n_y)
    namwoos = [n for n in list(additional_namwoo)]
    
    additional_ghosts = set()
    for ghost in ghosts:
        g_x, g_y = ghost
        vis[g_x][g_y] = 2
        mark_ghost(g_x, g_y)
    
    if len(additional_namwoo) == 0:
        print("No")
        break
    
    ghosts = [g for g in list(additional_ghosts)]    
    
    if matrix[exit_x][exit_y] == 'N':
        print("Yes")
        break
    if matrix[exit_x][exit_y] == 'G':
        print("No")
        break