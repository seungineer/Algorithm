import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(str, input().strip())))

flag = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'I':
            st_i, st_j = i, j
            flag = True
            break
    if flag:
        break

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

wait_lst = deque()    

wait_lst.append([st_i, st_j])
cnt = 0
while wait_lst:
    x, y = wait_lst.popleft()
    if x < 0 or n <= x or y < 0 or m <= y:
        continue
    if matrix[x][y] == 'Z':
        continue
    if matrix[x][y] == 'X':
        continue
    if matrix[x][y] == 'P':
        cnt += 1
    matrix[x][y] = 'Z'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        wait_lst.append([nx, ny])

if cnt == 0:
    print('TT')
else:
    print(cnt)