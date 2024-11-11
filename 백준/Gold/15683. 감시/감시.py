# 1~5가 위치한 곳 어떤 커맨드가 들어갈지 dfs로 결정
# 모든 cctv에 어떤 커맨드가 들어갈지 결정되면
## 사각지대 개수 세기
## 개수 다 셌으면 # 없는 새걸로 갈아 끼우기

N, M = map(int, input().split())
original_matrix = [list(map(int, input().split())) for _ in range(N)]

dir1 = [['up'], ['down'], ['left'], ['right']]
dir2 = [['up', 'down'], ['left', 'right']]
dir3 = [['up', 'right'], ['up', 'left'], ['down', 'right'], ['down', 'left']]
dir4 = [['up', 'down', 'right'], ['up', 'down', 'left'], ['left', 'right', 'up'], ['left', 'right', 'down']]
dir5 = [['up', 'down', 'right', 'left']]
command_lst = [dir1, dir2, dir3, dir4, dir5]

def move(command):
    if command == 'up':
        return [-1, 0]
    if command == 'down':
        return [1, 0]
    if command == 'left':
        return [0, -1]
    if command == 'right':
        return [0, 1]

def count(draw_matrix):
    count = 0
    for i in range(N):
        for j in range(M):
            if draw_matrix[i][j] == 0 and original_matrix[i][j] == 0: count += 1
    min_count[0] = min(min_count[0], count)


def draw(x, y, command, draw_matrix):
    draw_matrix[x][y] = 9
    for direction_str in command:
        nx, ny = x, y
        while (0 <= nx and nx < N) and (0 <= ny and ny < M) and original_matrix[nx][ny] != 6:
            draw_matrix[nx][ny] = 9
            dx, dy = move(direction_str)
            nx += dx
            ny += dy

def drawAndCount(qu):
    draw_matrix = [[0 for _ in range(M)] for _ in range(N)]
    for q in qu:
        x, y, command = q
        draw(x, y, command, draw_matrix)
    count(draw_matrix)
    return
    

def dfs(qu):
    if len(qu) == cctv_cnt[0]:
        drawAndCount(qu)
        return
    isEnd = False
    for i in range(N):
        for j in range(M):
            if original_matrix[i][j] in [1,2,3,4,5] and vis[i][j] == 0:
                for dir_lst in command_lst[original_matrix[i][j] - 1]:
                    vis[i][j] = 1
                    qu.append([i, j, dir_lst])
                    dfs(qu)
                    qu.pop()
                    vis[i][j] = 0
                isEnd = True
            if isEnd : break
        if isEnd : break
    return

cctv_cnt = [0]
wall_cnt = [0]
for i in range(N):
    for j in range(M):
        if original_matrix[i][j] in [1,2,3,4,5]: cctv_cnt[0] += 1
        if original_matrix[i][j] == 6: wall_cnt[0] += 1

vis = [[0 for _ in range(M)] for _ in range(N)]
min_count = [1e9]
isEnd = False
for i in range(N):
    for j in range(M):
        if original_matrix[i][j] in [1,2,3,4,5]:
            for dir_lst in command_lst[original_matrix[i][j] - 1]:
                vis[i][j] = 1
                qu = [[i, j, dir_lst]]
                dfs(qu)
            isEnd = True
        if isEnd: break
    if isEnd: break

if min_count[0] == 1e9: print(N*M - cctv_cnt[0] - wall_cnt[0])
else: print(min_count[0])

            