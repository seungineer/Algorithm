import sys
from collections import deque
input = sys.stdin.readline
matrix = [list(map(str, input().rstrip())) for _ in range(12)]

def BFS(color, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    qu = deque()
    qu.append((x, y))
    break_cnt = 0
    vis = [[0 for _ in range(6)] for _ in range(12)]
    while qu:
        x, y = qu.popleft()
        vis[x][y] = 1
        break_cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < 12 and 0 <= ny and ny < 6:
                if vis[nx][ny] == 0 and matrix[nx][ny] == color:
                    vis[nx][ny] = 1
                    qu.append((nx, ny))
    if break_cnt < 4:
        return
    is_broken[0] = True
    qu = deque()
    qu.append((x, y))
    while qu:
        x, y = qu.popleft()
        breaks[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < 12 and 0 <= ny and ny < 6:
                if breaks[nx][ny] == 0 and matrix[nx][ny] == color:
                    breaks[nx][ny] = 1
                    qu.append((nx, ny))

def fall_blocks():
    for j in range(6):
        qu = deque()
        cnt = 0
        for i in range(11, -1, -1):
            if matrix[i][j] == '.':
                cnt += 1
                continue
            qu.append(matrix[i][j])
        if cnt > 0:
            for _ in range(cnt):
                qu.append('.')
        
        for i in range(11, -1, -1):
            matrix[i][j] = qu.popleft()

iter_cnt = 0
while True:
    # BFS로 터트릴 수 있는 블럭 찾기
    breaks = [[0 for _ in range(6)] for _ in range(12)]
    is_broken = [False]
    for i in range(12):
        for j in range(6):
            if matrix[i][j] == '.': continue
            BFS(matrix[i][j], i, j)
    if not is_broken[0]: break
    iter_cnt += 1
    # 터트리기
    for i in range(12):
        for j in range(6):
            if breaks[i][j] == 1:
                matrix[i][j] = '.'
    # 각 열별 블럭에 중력 반영하기
    fall_blocks()
    
print(iter_cnt)