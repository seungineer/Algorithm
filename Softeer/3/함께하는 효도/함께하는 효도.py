import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
friends = []
for _ in range(M):
    st_x, st_y = map(int, input().split())
    friends.append([st_x - 1, st_y - 1])

answer = [0]
def dfs2(x, y, score, depth, manIdx):
    if depth == 4:
        if manIdx == M-1: answer[0] = max(answer[0], score)
        else:
            friend = friends[manIdx + 1]
            dfs2(friend[0], friend[1], score + matrix[friend[0]][friend[1]], 1, manIdx + 1)
        return
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if vis[nx][ny] == 0:
                vis[nx][ny] = 1
                dfs2(nx, ny, score + matrix[nx][ny], depth + 1, manIdx)
                vis[nx][ny] = 0
    
def dfs(x, y, score, depth, manIdx):
    if depth == 4:
        if manIdx == M - 1: answer[0] = max(answer[0], score)
        else:
            friend = friends[manIdx + 1]
            dfs2(friend[0], friend[1], score + matrix[friend[0]][friend[1]], 1, manIdx + 1)
        return
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if vis[nx][ny] == 0:
                vis[nx][ny] = 1
                dfs(nx, ny, score + matrix[nx][ny], depth + 1, manIdx)
                vis[nx][ny] = 0

vis = [[0 for _ in range(N)] for _ in range(N)]
for friend in friends:
    x, y = friend[0], friend[1]
    vis[x][y] = 1

dfs(friends[0][0], friends[0][1], matrix[friends[0][0]][friends[0][1]], 1, 0)
print(answer[0])