import sys
sys.setrecursionlimit(10**6)

while True:
    w, h = map(int, input().split())

    if w==0 and h==0:
        break
    graph = []

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    def dfs(i, j):
        if i < 0 or h<= i or j < 0 or w<= j:
            return
        if graph[i][j] == 0:
            return
        graph[i][j] = 0
        dx = [1, 0, -1, 0, 1, 1, -1, -1]
        dy = [0, 1, 0, -1, 1, -1, 1, -1]

        for m in range(8):
            nx = i + dx[m]
            ny = j + dy[m]
            dfs(nx, ny)

    area_cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] ==1:
                area_cnt += 1
                dfs(i, j)
                
    print(area_cnt)
