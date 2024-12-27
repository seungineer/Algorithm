# 인접 마을 문 열기
## 문 하나라도 열지 않으면 break
## 문 하나라도 열면 cnt += 1
# 연합 계산하기

# 순회하면서 마을 문 열 때, info dict에 갯수와 total 정보 저장
# 모든 순회를 마치고, vis를 보면서 실제 matrix 업데이트 하기
from collections import deque
N, M, R = map(int, input().split())
matrix = []
for _ in range(N): matrix.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, mark):
    qu = deque()
    qu.append([i, j])
    sub_sum = 0
    cnt = 0
    while qu:
        i, j = qu.popleft()
        cnt += 1
        sub_sum += matrix[i][j]
        vis[i][j] = mark
        info[mark] = [sub_sum, cnt]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if vis[nx][ny] == 0:
                    diff = abs(matrix[i][j] - matrix[nx][ny])
                    if M <= diff and diff <= R:
                        hasUnion[0] = True
                        vis[nx][ny] = mark
                        qu.append([nx, ny])

iter_cnt = 0
while True:
    hasUnion = [False]
    vis = [[0 for _ in range(N)] for _ in range(N)]
    info = dict()
    mark = -1
    for i in range(N):
        for j in range(N):
            if vis[i][j] != 0: continue
            bfs(i, j, mark)
            mark -= 1
    if not hasUnion[0]: break
    iter_cnt += 1
    for i in range(N):
        for j in range(N):
            marked = vis[i][j]
            matrix[i][j] = info[marked][0] // info[marked][1]

print(iter_cnt)
