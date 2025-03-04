def solution():
    N = int(input())
    matrix = [list(map(str, input().split())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def hided(matrix):
        isHided = True
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 'S':
                    for k in range(4):
                        for length in range(1, N):
                            nx = i + dx[k] * length
                            ny = j + dy[k] * length
                            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                                if matrix[nx][ny] == 'T':
                                    isHided = False
                                if matrix[nx][ny] == 'O':
                                    break
        return isHided
    
    def bt(cnt):
        if cnt == 3:
            # yes인지 no인지 판단
            if hided(matrix):
                print("YES")
                exit()
            return
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 'O'
                    bt(cnt + 1)
                    matrix[i][j] = 'X'

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'X':
                matrix[i][j] = 'O'
                bt(1)
                matrix[i][j] = 'X'
    print("NO")
solution()