R, C, N = map(int, input().split())
matrix_even = [] # N-1//2 기준 0, 2, 4, 6 ...
for _ in range(R):
    matrix_even.append(list(map(str,input())))
matrix_odd = [['.' for _ in range(C)] for _ in range(R)]
#
if N % 2 == 0:
    temp = ['O' for _ in range(C)]
    for _ in range(R):
        print(''.join(map(str, temp)))
    exit()
#
target_cnt = (N-1)//2

def doSwap(m1, m2):
    # m1 매트릭스를 보고 m2를 수정해야 함
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(R):
        for j in range(C):
            if m1[i][j] == '.':
                hasBomb = False
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni and ni < R and 0 <= nj and nj < C:
                        if m1[ni][nj] == 'O':
                            hasBomb = True
                if hasBomb:
                    m2[i][j] = '.'
                else:
                    m2[i][j] = 'O'
            else:
                m2[i][j] = '.'

for cnt in range(target_cnt):
    if cnt % 2 == 0: # even
        doSwap(matrix_even, matrix_odd)
    else:
        doSwap(matrix_odd, matrix_even)

if target_cnt % 2 ==0:
    for m in matrix_even:
        print(''.join(map(str, m)))
else:
    for m in matrix_odd:
        print(''.join(map(str, m)))