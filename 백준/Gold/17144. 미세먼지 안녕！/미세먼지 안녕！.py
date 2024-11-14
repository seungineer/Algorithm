N, M, T = map(int, input().split())
original_matrix = [list(map(int, input().split())) for _ in range(N)]
up_machine = []
down_machine = []
for i in range(N):
    for j in range(M):
        if original_matrix[i][j] == -1:
            if len(up_machine) == 0:
                up_machine = [i, j]
            else:
                down_machine = [i, j]
for _ in range(T):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    delta = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if original_matrix[i][j] > 0:
                sub_sum = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx and nx < N and 0 <= ny and ny < M:
                        if original_matrix[nx][ny] != -1:
                            delta[nx][ny] += original_matrix[i][j] // 5
                            sub_sum += original_matrix[i][j] // 5
                delta[i][j] -= sub_sum
    for i in range(N):
        for j in range(M):
            original_matrix[i][j] += delta[i][j]

    # 윗 부분 순환
    up_x, up_y = up_machine
    up_dx = [-1, 0, 1, 0]
    up_dy = [0, 1, 0, -1]

    st_x, st_y = up_x, up_y
    for k in range(4):
        while True:
            prev_x, prev_y = st_x, st_y
            st_x += up_dx[k]
            st_y += up_dy[k]
            if not (0 <= st_x and st_x <= up_x and 0 <= st_y and st_y < M):
                st_x -= up_dx[k]
                st_y -= up_dy[k]
                break
            original_matrix[prev_x][prev_y] = original_matrix[st_x][st_y]
    original_matrix[up_x][up_y] = -1
    original_matrix[up_x][up_y+1] = 0

    # 아랫 부분 순환
    down_x, down_y = down_machine
    down_dx = [1, 0, -1, 0]
    down_dy = [0, 1, 0, -1]

    st_x, st_y = down_x, down_y
    for k in range(4):
        while True:
            prev_x, prev_y = st_x, st_y
            st_x += down_dx[k]
            st_y += down_dy[k]
            if not (down_x <= st_x and st_x < N and 0 <= st_y and st_y < M):
                st_x -= down_dx[k]
                st_y -= down_dy[k]
                break
            original_matrix[prev_x][prev_y] = original_matrix[st_x][st_y]
    original_matrix[down_x][down_y] = -1
    original_matrix[down_x][down_y+1] = 0
    # print(original_matrix)

answer = 0
for i in range(N):
    for j in range(M):
        if original_matrix[i][j] > 0: answer += original_matrix[i][j]
print(answer)
