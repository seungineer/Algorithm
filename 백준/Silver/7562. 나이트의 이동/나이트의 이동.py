from collections import deque
tc = int(input())
for _ in range(tc):
    I = int(input())
    st_x, st_y = map(int, input().split())
    en_x, en_y = map(int, input().split())

    vis = [[0 for _ in range(I)] for _ in range(I)]

    qu = deque()
    qu.append([st_x, st_y, 0])
    while qu:
        x, y, sec = qu.popleft()
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]
        if x == en_x and y== en_y: break
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < I and 0 <= ny and ny < I:
                if vis[nx][ny] == 0:
                    vis[nx][ny] = 1
                    qu.append([nx, ny, sec+1])
    print(sec)