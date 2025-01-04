def solution():
    N, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    row_plus = [[0 for _ in range(N)] for _ in range(N)]
    col_plus = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 길이 L만큼 확인한 후에 경사로 넣을 수 있으면 값 할당 로직으로 수정
            target = matrix[i][j]
            isCol = 0
            for dx in range(L):
                if i + dx >= N: break
                if target == matrix[i+dx][j]:
                    isCol += 1
            if isCol == L:
                for dx in range(L):
                    col_plus[i+dx][j] = matrix[i+dx][j] + 1
            
            isRow = 0
            for dy in range(L):
                if j + dy >= N: break
                if target == matrix[i][j+dy]:
                    isRow += 1
            if isRow == L:
                for dy in range(L):
                    row_plus[i][j+dy] = matrix[i][j+dy] + 1
            
    # 행에서 건널 수 있는 다리 개수 카운트
    row_cnt = 0
    row_vis = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        canGo = True
        for j in range(N-1):
            # i,j보다 1 크, 작, 같 또는 1보다 큰 차이
            if not canGo: break
            if j+1 < N and row_vis[i][j] != 0: row_vis[i][j+1] = row_vis[i][j] - 1
            
            if abs(matrix[i][j] - matrix[i][j+1]) > 1: canGo = False
            
            if matrix[i][j] == matrix[i][j+1] + 1:
                if row_vis[i][j+1] == 0 and matrix[i][j] == row_plus[i][j+1]:
                    row_vis[i][j+1] = L
                else: canGo = False
                
            if matrix[i][j] == matrix[i][j+1] - 1:
                if sum(row_vis[i][j-L+1:j+1]) != 0 or row_plus[i][j] != matrix[i][j+1]:
                    canGo = False
        if canGo: row_cnt += 1
        
        
    # 열에서 건널 수 있는 다리 개수 카운트
    col_cnt = 0
    col_vis = [[0 for _ in range(N)] for _ in range(N)]
    
    for j in range(N):
        canGo = True
        for i in range(N-1):
            # i,j보다 1 크, 작, 같 또는 1보다 큰 차이
            if not canGo: break

            if i + 1 < N and col_vis[i][j] != 0: col_vis[i+1][j] = col_vis[i][j] - 1
            
            if abs(matrix[i][j] - matrix[i+1][j]) > 1: canGo = False
            
            if matrix[i][j] == matrix[i+1][j] + 1:
                if col_vis[i+1][j] == 0 and matrix[i][j] == col_plus[i+1][j]:
                    col_vis[i+1][j] = L
                else: canGo = False
            if matrix[i][j] == matrix[i+1][j] - 1:
                tot = 0
                for temp in range(i-L+1, i+1):
                    if temp < 0: continue
                    tot += col_vis[temp][j]
                if tot != 0 or col_plus[i][j] != matrix[i+1][j]:
                    canGo = False
        if canGo: col_cnt += 1

    print(row_cnt + col_cnt)
    return

solution()
