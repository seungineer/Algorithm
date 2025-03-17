def solution():
    R, C, K = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(R)]
    cnt = [0]
    def dfs(x, y, depth):
        if x == 0 and y == C-1 and depth == K:
            cnt[0] += 1
            return
        if depth >= K:
            return
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 > nx or 0 > ny or nx >= R or ny >= C: continue
            if vis[nx][ny] == 0 and matrix[nx][ny] == '.':
                vis[nx][ny] = 1
                dfs(nx, ny, depth + 1)
                vis[nx][ny] = 0

    vis = [[0 for _ in range(C)] for _ in range(R)]
    vis[R-1][0] = 1
    dfs(R-1, 0, 1)
    print(cnt[0])

solution()