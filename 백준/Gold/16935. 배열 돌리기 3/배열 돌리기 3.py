def solution():
    N, M, R = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    seq = list(map(int, input().split()))

    def operation(command):
        # 3, 4는 90도 회전으로 인해 매트릭스 크기 변경될 수 있음
        if command in [1, 2, 5, 6]:
            temp = [[0 for _ in range(M)] for _ in range(N)]
        else:
            temp = [[0 for _ in range(N)] for _ in range(M)]
        if command == 1:
            for i in range(N):
                for j in range(M):
                    temp[-i-1][j] = matrix[i][j]
        if command == 2:
            for i in range(N):
                for j in range(M):
                    temp[i][-j-1] = matrix[i][j]
        if command == 3:
            for i in range(N):
                for j in range(M):
                    temp[j][-i-1] = matrix[i][j]
        if command == 4:
            for i in range(N):
                for j in range(M):
                    temp[-j-1][i] = matrix[i][j]
        if command == 5 or command == 6:
            # A | B
            # D | C
            groupA = [[matrix[i][j] for j in range(M//2)] for i in range(N//2)]
            groupB = [[matrix[i][j] for j in range(M//2, M)] for i in range(N//2)]
            groupC = [[matrix[i][j] for j in range(M//2, M)] for i in range(N//2, N)]
            groupD = [[matrix[i][j] for j in range(M//2)] for i in range(N//2, N)]
            if command == 5:
                for i in range(N):
                    for j in range(M):
                        if i < N//2:
                            # A or D
                            if j < M//2:
                                # D
                                temp[i][j] = groupD[i][j]
                            else:
                                # A
                                temp[i][j] = groupA[i][j-M//2]
                        else:
                            # B or C
                            if j < M//2:
                                # C
                                temp[i][j] = groupC[i-N//2][j]
                            else:
                                # B
                                temp[i][j] = groupB[i-N//2][j-M//2]
            if command == 6:
                for i in range(N):
                    for j in range(M):
                        if i < N//2:
                            # B or C
                            if j < M//2:
                                # B
                                temp[i][j] = groupB[i][j]
                            else:
                                # C
                                temp[i][j] = groupC[i][j-M//2]
                        else:
                            # A or D
                            if j < M//2:
                                # A
                                temp[i][j] = groupA[i-N//2][j]
                            else:
                                # D
                                temp[i][j] = groupD[i-N//2][j-M//2]
        return temp


    for command in seq:
        res = operation(command)
        matrix = res
        N, M = len(matrix), len(matrix[0])
    for row in matrix:
        print(*row)
    return
solution()