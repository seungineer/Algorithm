from collections import deque
m, n = map(int, input().split())
#     m(x) ....
# n(y)
# .
# .
# .
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
wait_list = deque()
vis = [[0 for _ in range(m)]for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            wait_list.append([i, j, 0])
            vis[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def is_range(x, y):
    return 0<= x < m and 0<= y < n

max_cnt = -1
while wait_list:
    y, x, cnt = wait_list.popleft()
    matrix[y][x] = -1
    max_cnt = max(cnt, max_cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if is_range(nx, ny) and vis[ny][nx] == 0 and matrix[ny][nx] != -1:
            wait_list.append([ny, nx, cnt + 1])
            vis[ny][nx] = 1
flag = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            flag = True
if flag :
    print(-1)
else:
    print(max_cnt)