matrix = []
for _ in range(9):
    matrix.append(list(map(int, input())))

def isValid(i,j,cand):
    for a in range(9):
        if matrix[a][j] == cand or matrix[i][a] == cand:
            return False
    start_row = 3 * (i//3)
    start_col = 3 * (j//3)
    for a in range(start_row, start_row+3):
        for b in range(start_col, start_col+3):
            if matrix[a][b] == cand:
                return False
    return True

def f():
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                for cand in range(1, 10):
                    if isValid(i,j,cand):
                        matrix[i][j] = cand
                        if f():
                            return True
                        matrix[i][j] = 0
                return False
    return True

f()
for i in range(9):
    print(''.join(map(str, matrix[i])))