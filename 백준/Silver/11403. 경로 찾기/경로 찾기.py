n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

vis = [[0 for _ in range(n)]for _ in range(n)]
temp = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            vis[i][j] = 1
            temp.append(j)
    while temp:
        st = temp.pop()
        for k in range(n):
            if vis[i][k] == 1:
                continue
            if matrix[st][k] == 1:
                vis[i][k] = 1
                temp.append(k)
for lst in vis:
    print(*lst)
        

