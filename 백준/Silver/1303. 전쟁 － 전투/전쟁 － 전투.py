from collections import deque
def solution():
    M, N = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(N)]

    def bfs(x, y, target):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        qu = deque()
        qu.append((x, y))

        vis[x][y] = 1
        while qu:
            x, y = qu.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 > nx or N <= nx or 0 > ny or M <= ny: continue
                if matrix[nx][ny] == target and vis[nx][ny] == 0:
                    vis[nx][ny] = 1
                    cnt[0] += 1
                    qu.append((nx, ny))

    ans_w = 0
    vis = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W' and vis[i][j] == 0:
                cnt = [1]
                bfs(i, j, 'W')
                ans_w += cnt[0] ** 2
    ans_b = 0
    vis = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'B' and vis[i][j] == 0:
                cnt = [1]
                bfs(i, j, 'B')
                ans_b += cnt[0] ** 2
    print(ans_w, ans_b)

solution()