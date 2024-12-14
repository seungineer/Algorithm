import heapq as hq
N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
vis = [[-1 for _ in range(N)] for _ in range(N)]

wait_lst = []
ST_X, ST_Y = 0, 0
EN_X, EN_Y = N-1, N-1

hq.heappush(wait_lst, [0, 0, ST_X, ST_Y])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while wait_lst:
    break_cnt, distance, x, y = hq.heappop(wait_lst)
    vis[x][y] = break_cnt
    if x == EN_X and y == EN_Y:
        print(break_cnt)
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if vis[nx][ny] != -1: continue
            if matrix[nx][ny] == 1:
                vis[nx][ny] = break_cnt
                hq.heappush(wait_lst, [break_cnt, distance + 1, nx, ny])
            else:
                vis[nx][ny] = break_cnt + 1
                hq.heappush(wait_lst, [break_cnt + 1, distance + 1, nx, ny])
