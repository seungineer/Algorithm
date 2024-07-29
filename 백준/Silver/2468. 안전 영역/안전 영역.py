from collections import deque
n = int(input())
maxh = -float("inf")
minh = float("inf")
matrix = []
for _ in range(n):
    lst = list(map(int, input().split()))
    matrix.append(lst)
    maxh = max(maxh, max(lst))
    minh = min(minh, min(lst))


def countArea(matrix, height):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    area_cnt = 0
    for i in range(n):
        for j in range(n):
            if vis[i][j] == False and matrix[i][j] > height:
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if  0 <= nx < n and 0<= ny < n and vis[nx][ny] == False and matrix[nx][ny] > height:
                            queue.append([nx,ny])
                            vis[nx][ny] = True
                area_cnt += 1
    if area_cnt == 0:
        area_cnt = 1
    return area_cnt

# prev_cnt = 1
max_cnt = -1
for height in range(minh, maxh+1):
    vis = [[False for _ in range(n)]for _ in range(n)]
    max_cnt = max(max_cnt, countArea(matrix, height))
    # if prev_cnt <= cur_cnt:
    #     prev_cnt = cur_cnt
    #     continue
    # else:
    #     break
print(max_cnt)