while True:
    seq = list(map(str, input()))
    if seq[0] == "e": break
    matrix = []
    for temp in range(3):
        matrix.append(list(seq[3*temp:3*temp+3]))

    o_cnt = 0
    x_cnt = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 'O':
                o_cnt += 1
            elif matrix[i][j] == 'X':
                x_cnt += 1
    # x 한 줄 있는지 찾기 dfs로 0~7 중 몇 번으로 계속 들어가서 isFind True로
    isFindx = [False]
    isFindy = [False]
    def dfs(x, y, cnt, direction, target):
        if cnt == 3:
            if target == 'X' :
                isFindx[0] = True
            else:
                isFindy[0] = True
            return

        dx = [-1, 0, 1, -1, 0, 1, 1, -1]
        dy = [1, 1, 1, -1, -1, -1, 0, 0]
        if direction == 8:
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx and nx < 3 and 0 <= ny and ny < 3:
                    if matrix[nx][ny] == target and (direction == 8 or direction == k):
                        dfs(nx, ny, cnt+1, k, target)
        else:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx and nx < 3 and 0 <= ny and ny < 3:
                if matrix[nx][ny] == target :
                    dfs(nx, ny, cnt+1, direction, target)
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 'X':
                dfs(i,j,1,8,'X')
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 'O':
                dfs(i,j,1,8,'O')
    
    # x가 한 줄 완성된 경우 -> x가 한 개 더 많아야 yes 아니면 no
    # o가 한 줄 완성된 경우 -> o의 개수는 x와 같아야 yes 아니면 no
    if isFindx[0] == True:
        if x_cnt == o_cnt + 1 and not isFindy[0]:
            print("valid")
            continue
        else:
            print("invalid")
            continue
    if isFindy[0] == True:
        if x_cnt == o_cnt:
            print("valid")
            continue
        else:
            print("invalid")
            continue

    # x or o가 다 완성되지 않은 경우
    if x_cnt == 5 and o_cnt == 4:
        print("valid")
    else:
        print("invalid")
    