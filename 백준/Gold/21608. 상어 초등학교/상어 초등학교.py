def solution():
    N = int(input())
    input_lst = [list(map(int, input().split())) for _ in range(N**2)]
    favorites = dict()
    for i in range(len(input_lst)):
        favorites[input_lst[i][0]] = set(input_lst[i][1:])
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    
    def find_best_blank(target):
        count_best = [[0 for _ in range(N)] for _ in range(N)]
        count_blank = [[0 for _ in range(N)] for _ in range(N)]
        max_best = -1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for x in range(N):
            for y in range(N):
                if matrix[x][y] != 0: continue
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx and nx < N and 0 <= ny and ny < N:
                        if matrix[nx][ny] == 0:
                            count_blank[x][y] += 1
                        if matrix[nx][ny] in favorites[target]:
                            count_best[x][y] += 1
                            max_best = max(max_best, count_best[x][y])
                            
        bests = []
        for i in range(N):
            for j in range(N):
                if matrix[i][j] != 0: continue
                if count_best[i][j] == max_best:
                    bests.append((i,j))
        return bests, count_blank
    
    def count_satisfaction(matrix):
        points = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for x in range(N):
            for y in range(N):
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx and nx < N and 0 <= ny and ny < N:
                        if matrix[nx][ny] in favorites[matrix[x][y]]:
                            cnt += 1
                if cnt == 1: points += 1
                if cnt == 2: points += 10
                if cnt == 3: points += 100
                if cnt == 4: points += 1000
        return points
                
    
    for i in range(len(input_lst)):
        target = input_lst[i][0]
        bests, count_blank = find_best_blank(target)
        if len(bests) > 1:
            max_blank = -1
            target_x, target_y = -1, -1
            for x, y in bests:
                if count_blank[x][y] > max_blank:
                    max_blank = count_blank[x][y]
                    target_x, target_y = x, y
            matrix[target_x][target_y] = target
            continue
        if len(bests) == 1:
            target_x, target_y = bests[0]
            matrix[target_x][target_y] = target
            continue
        # bests가 없는 경우
        max_blank = -1
        target_x, target_y = -1, -1
        for i in range(N):
            for j in range(N):
                if matrix[i][j] != 0: continue
                if count_blank[i][j] > max_blank:
                    max_blank = count_blank[i][j]
                    target_x, target_y = i, j
        matrix[target_x][target_y] = target
    
    print(count_satisfaction(matrix))
    return
solution()