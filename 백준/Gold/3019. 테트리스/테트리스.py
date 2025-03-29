def solution():
    C, P = map(int, input().split())
    seq = list(map(int, input().split()))
    matrix = [[0 for _ in range(C)] for _ in range(105)]
    for j in range(C): matrix[0][j] = 1
    for j in range(C):
        height = seq[j]
        for i in range(1, height + 1):
            matrix[i][j] = 1
    p1 = [[1,0], [2,0], [3,0]]
    p2 = [[1,0], [0,1], [1,1]]
    p3 = [[0,1], [1,1], [1,2]]
    p4 = [[1,0], [1,1], [2,1]]
    p5 = [[0,1], [1,1], [0,2]]
    p6 = [[0,1], [0,2], [1,2]]
    p7 = [[1,0], [0,1], [0,2]]
    delta = [p1, p2, p3, p4, p5, p6, p7]
    directions = [[[1, 0], [0, 1]], [[0, -1], [1, 0]], [[-1, 0], [0, -1]], [[0, 1], [-1, 0]]]

    def transform(st_x, st_y, x, y, direction):
        nx = st_x + (x - st_x) * directions[direction][0][0] + (y - st_y) * directions[direction][0][1]
        ny = st_y + (x - st_x) * directions[direction][1][0] + (y - st_y) * directions[direction][1][1]
        return nx, ny

    def clearMark(x, y, p, direction):
        matrix[x][y] = 0
        for k in range(3):
                nx = x + delta[p][k][0]
                ny = y + delta[p][k][1]
                nx, ny = transform(x, y, nx, ny, direction)
                if 0 <= nx < 105 and 0 <= ny < C:
                    matrix[nx][ny] = 0

    def isValid(x, y, p, direction):
        # 겹치는 경우 확인
        for k in range(3):
            nx = x + delta[p][k][0]
            ny = y + delta[p][k][1]
            nx, ny = transform(x, y, nx, ny, direction)
            if 0 <= nx < 105 and 0 <= ny < C:
                if matrix[nx][ny] == 1: return False
        # 뛰어져 있는 경우 확인
        isOutBound = False
        for k in range(3):
            nx = x + delta[p][k][0]
            ny = y + delta[p][k][1]
            nx, ny = transform(x, y, nx, ny, direction)
            if 0 <= nx < 105 and 0 <= ny < C:
                matrix[nx][ny] = 1
            else:
                isOutBound = True
        if isOutBound:
            clearMark(x, y, p, direction)
            return False
        else:
            # 열의 모든 1을 다 더한 값이 max_i와 같은지 확인
            isBlank = False
            heights = []
            for j in range(C):
                max_i = -1
                cnt1 = 0
                for i in range(105):
                    if matrix[i][j] == 1:
                        cnt1 += 1
                        max_i = max(max_i, i+1)
                if cnt1 != max_i:
                    isBlank = True
                    break
                heights.append(max_i)
            # 원상복귀
            # print(isBlank)
            # print(matrix)
            clearMark(x, y, p, direction)
            if isBlank: return False
        if tuple(heights) in finds: return False
        finds.add(tuple(heights))
        return True

    # 기존 블럭 최상단에서 4바퀴 회전 수행
    ans = 0
    finds = set()
    for st_j in range(C):
        for k in range(1, 5):
            st_i = seq[st_j] + k
            for dir in range(4):
                matrix[st_i][st_j] = 1
                if isValid(st_i, st_j, P-1, dir): ans += 1
                matrix[st_i][st_j] = 0
    print(ans)

solution()