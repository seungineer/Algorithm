from collections import deque
R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

def bfs(start, end):
    st, en = start, end
    queue = deque()
    queue.append([st, en])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < R and 0 <= ny and ny < C:
                if matrix[nx][ny] != 1 and air[nx][ny] == 0:
                    air[nx][ny] = 1
                    queue.append([nx, ny])

iter_cnt = 0
while True:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 공기 살포(BFS)
    air = [[0 for _ in range(C)] for _ in range(R)]
    bfs(0, 0)


    cnt_1 = 0
    isStop = True
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0: continue
            cnt_1 += 1
            isStop = False
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx and nx < R and 0 <= ny and ny < C:
                    if air[nx][ny] == 1:
                        matrix[i][j] = 0
    if isStop: break
    iter_cnt += 1
    prev_cnt_1 = cnt_1

print(iter_cnt)
print(prev_cnt_1)
