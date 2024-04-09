t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    matrix = [[0 for _ in range(m+2)] for _ in range(n+2)]
    # matrix내 상하좌우 버퍼 한 줄 씩 존재

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    lst = []
    for i in range(k):
        a, b = map(int, input().split())
        matrix[b+1][a+1] = 1

    def bfs(x, y):
        if not(x >= 1 and m+1 >= x and y>= 1 and y<= n+1):
            return # 범위 밖이면 리턴
        
        if matrix[y][x] != 1:
            return # 0이면 리턴
        else: 
            matrix[y][x] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                bfs(nx, ny)
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i][j] == 1:
                bfs(j, i)
                cnt += 1

    print(cnt)