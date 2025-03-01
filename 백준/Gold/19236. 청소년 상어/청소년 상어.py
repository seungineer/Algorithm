matrix = []
direction = []
for _ in range(4):
    a, ad, b, bd, c, cd, d, dd = map(int, input().split())
    matrix.append([a, b, c, d])
    direction.append([ad-1, bd-1, cd-1, dd-1])
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def fish_move():
    # 물고기 숫자 순서대로 스와핑
    # 상어가 있으면 회전해서라도 이동
    global matrix
    cand = set()
    for i in range(4):
        for j in range(4):
            if matrix[i][j] not in range(1, 17): continue
            cand.add(matrix[i][j])
    
    for org_number in sorted(cand):
        is_swapped = False
        for i in range(4):
            for j in range(4):
                if matrix[i][j] != org_number: continue
                org_dir = direction[i][j]
                for k in range(8):
                    if is_swapped: break
                    nx = i + dx[(org_dir + k)%8]
                    ny = j + dy[(org_dir + k)%8]
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if matrix[nx][ny] != -1:
                            # 스와핑
                            is_swapped = True
                            matrix[i][j], matrix[nx][ny] = matrix[nx][ny], matrix[i][j]
                            direction[i][j], direction[nx][ny] = direction[nx][ny], (org_dir + k)%8

def shark_move(x, y):
    global direction
    global matrix
    sharks_dir = direction[x][y]
    org_matrix = [[matrix[i][j] for j in range(4)] for i in range(4)]
    org_direction = [[direction[i][j] for j in range(4)] for i in range(4)]
    fish_move()
    matrix[x][y] = 0
    for distance in range(1, 4):
        nx = x + dx[sharks_dir] * distance
        ny = y + dy[sharks_dir] * distance
        if 0 <= nx < 4 and 0 <= ny < 4:
            if matrix[nx][ny] not in range(1, 17): continue
            org_fish = matrix[nx][ny]
            points[0] += org_fish
            matrix[nx][ny] = -1
            ans[0] = max(ans[0], points[0])
            shark_move(nx, ny)
            matrix[nx][ny] = org_fish
            points[0] -= org_fish
    # 매트릭스, direction 원복 필요
    matrix = [[org_matrix[i][j] for j in range(4)] for i in range(4)]
    direction = [[org_direction[i][j] for j in range(4)] for i in range(4)]

ans = [matrix[0][0]]
# 상어 (0, 0)으로 이동
points = [matrix[0][0]]
matrix[0][0] = -1 # 상어 표시
sharks_dir = direction[0][0]
# 모든 물고기 이동
fish_move()
matrix[0][0] = 0
direction[0][0] = 0
for distance in range(1, 4):
    nx = 0 + dx[sharks_dir] * distance
    ny = 0 + dy[sharks_dir] * distance
    if 0 <= nx < 4 and 0 <= ny < 4:
        if matrix[nx][ny] not in range(1, 17): continue
        # 상어 이동 가능한 경우
        org_fish = matrix[nx][ny]
        points[0] += org_fish
        matrix[nx][ny] = -1
        ans[0] = max(ans[0], points[0])
        shark_move(nx, ny)
        # 상어 및 물고기 위치 원복
        ## 상어가 이동한 곳에 대한 정보를 저장해두고, 원복시켜야함
        matrix[nx][ny] = org_fish
        points[0] -= org_fish

print(ans[0])