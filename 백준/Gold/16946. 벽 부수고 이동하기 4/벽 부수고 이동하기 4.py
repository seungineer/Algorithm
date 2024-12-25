from collections import deque
N, M = map(int, input().split())
matrix = []
for _ in range(N): matrix.append(list(map(int, input())))

mark_cnt = dict()

def BFS(x, y, mark, cnt):
    qu = deque()
    qu.append([x, y])
    matrix[x][y] = mark

    while qu:
        x, y = qu.popleft()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = mark
                    qu.append([nx, ny])
    mark_cnt[mark] = cnt % 10

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

mark = -1
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            BFS(i, j, mark, 0)
            mark -= 1

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            marked = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx and nx < N and 0 <= ny and ny < M:
                    if matrix[nx][ny] < 0:
                        new_mark = matrix[nx][ny]
                        if new_mark in marked: continue
                        marked.add(new_mark)
                        matrix[i][j] += mark_cnt[new_mark]
            matrix[i][j] %= 10

for i in range(N):
    for j in range(M):
        if matrix[i][j] < 0: matrix[i][j] = 0

for el in matrix: print(''.join(map(str,el)))