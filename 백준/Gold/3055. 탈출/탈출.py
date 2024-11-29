import sys
sys.setrecursionlimit(10**6)
R, C = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(R)]
water_x, water_y = -1, -1
waters = []
for i in range(R):
    for j in range(C):
        if matrix[i][j] == '*': waters.append([i, j])
        if matrix[i][j] == 'S': mouse_x, mouse_y = i, j

# water에서 BFS 시작
def bfs_water(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < R and 0 <= ny and ny < C:
            if matrix[nx][ny] == '*' and vis[nx][ny] == 0:
                vis[nx][ny] = 1
                bfs_water(nx, ny)
            if matrix[nx][ny] == '.':
                vis[nx][ny] = '*'

def bfs_mouse(x, y):
    if x == -1 and y == -1: return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # print(x, y)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < R and 0 <= ny and ny < C:
            if matrix[nx][ny] == '.':
                candidates.add((nx, ny))
            
            if matrix[nx][ny] == 'D':
                isFind[0] = True


survives = set()
survives.add((mouse_x, mouse_y))
answer = 0
while True:
    # 물 범람 1회            
    vis = [[0 for _ in range(C)] for _ in range(R)]
    for water in waters:
        bfs_water(water[0], water[1])
    for i in range(R):
        for j in range(C):
            if vis[i][j] == '*': matrix[i][j] = '*'

    # 마우스 이동
    candidates = set()
    isFind = [False]
    isAdded = False
    answer += 1
    for i in range(len(list(survives))):
        x, y = list(survives)[i]
        bfs_mouse(x, y)
    survives = set()
    for el in list(candidates):
        isAdded = True
        survives.add(el)
    if isFind[0] == True:
        print(answer)
        exit()
    if not isAdded: break
print("KAKTUS")