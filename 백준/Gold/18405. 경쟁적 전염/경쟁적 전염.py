from collections import deque
def solution():
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split()) # 전염횟수
    X, Y = X - 1, Y - 1 # 도달위치

    qu = deque()
    # 바이러스를 숫자 순서대로 넣기
    starts = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                starts.append((matrix[i][j], i, j))
    starts.sort()
    vis = [[0 for _ in range(N)] for _ in range(N)]
    for s in starts:
        qu.append((s[0], s[1], s[2], 0)) # 종류, 위치x, 위치y, 전염진행횟수

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while qu:
        num, x, y, time = qu.popleft()
        if x == X and y == Y:
            print(num)
            exit()
        vis[x][y] = 1
        matrix[x][y] = num
        if time == S: continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if vis[nx][ny] == 0 and matrix[nx][ny] == 0:
                    vis[nx][ny] = 1
                    matrix[nx][ny] = num
                    qu.append((num, nx, ny, time+1))
    print(0)

solution()