# 상어는 자기보다 작은 물고기만 먹으며 지나갈 수 있음
# 상어는 자기와 같은 물고기는 지나갈수만 있음
# 상어는 자기보다 큰 물고기는 못 감

# 최초 상어 크기 2
# 먹을 수 있는 거리가 가까운 물고기가 많은 경우 가장 위, 가장 위에서 왼쪽 순으로 먹음
import heapq
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def bfs(st_i, st_j, size, eat):
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    candidate = []
    heapq.heappush(candidate, [0, st_i, st_j, 0]) # [거리, i(상하), j(좌우), 시간] 시작지점 주입
    vis[st_i][st_j] = 1
    matrix[st_i][st_j] = 0
    curr_size = size
    isEat = False
    while candidate:
        distance, i, j, cnt = heapq.heappop(candidate)
        if matrix[i][j] != 0 and matrix[i][j] != 9 and matrix[i][j] < curr_size:
            eat += 1
            isEat = True
            matrix[i][j] = 9
            if eat // curr_size == 1:
                curr_size += 1
                eat = 0
            break
        
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni and ni < N and 0 <= nj and nj < N:
                if vis[ni][nj] == 0 and matrix[ni][nj] <= curr_size:
                    vis[ni][nj] = 1
                    heapq.heappush(candidate, [distance + 1, ni, nj, cnt + 1])
    if not isEat: cnt = 0
    return curr_size, cnt, eat

size = 2
ans = 0
ate = 0
while True:
    isFind = False
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                vis = [[0 for _ in range(N)] for _ in range(N)]
                size, count, ate = bfs(i,j, size, ate)
                ans += count
                isFind = True
    if not isFind: break
print(ans)