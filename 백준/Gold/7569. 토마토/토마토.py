import sys
from collections import deque
input = sys.stdin.readline
col, row, height = map(int, input().split())
square = []
cube = [[] for _ in range(height)] # [height][row][col] 순으로 접근
for i in range(height):
    for _ in range(row):
        cube[i].append(list(map(int,input().split())))

queue = deque()
t = 0
for h in range(height):
    for r in range(row):
        for c in range(col):
            if cube[h][r][c] == 1:
                queue.append([h, r, c])

dh = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

max_cnt = -float("inf")
while queue:
    h, r, c = map(int, queue.popleft())
    for t in range(6):
        nh = h + dh[t]
        nr = r + dr[t]
        nc = c + dc[t]
        if (0<=nh) and (nh<height) and (0<=nr) and (nr<row) and (0<=nc) and (nc<col) and cube[nh][nr][nc] == 0:
            cube[nh][nr][nc] = cube[h][r][c] + 1
            queue.append((nh,nr,nc))

isImpossible = False
day = 0
for l in cube:
    for m in l:
        if 0 in m:
            isImpossible = True
            print(-1)
            break
        day = max(day, max(m))
    if isImpossible:
        break

if not isImpossible:
    print(day-1)