from collections import deque
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
wait_list = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j]==2:
            st_x, st_y = i, j
            wait_list.append([st_x, st_y, 0])
            break
vis = [[0 for _ in range(m)] for _ in range(n)]
#   y(j, m) ...
# x(i, n)
# .
# .
# .

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < m

while wait_list:
    pos = wait_list.popleft()
    matrix[pos[0]][pos[1]] = pos[2] # 시작 지점과의 거리
    for i in range(4):
        ny = pos[1] + dy[i]
        nx = pos[0] + dx[i]
        ncnt = pos[2] - 1
        if not is_range(nx, ny):
            continue
        if vis[nx][ny] == 1:
            continue
        if matrix[nx][ny] != 1:
            continue
        wait_list.append([nx, ny, ncnt])
        vis[nx][ny] = 1 # 방문 표시

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            print(-1, end= ' ')
        else:
            print(-matrix[i][j], end=' ')
    print()