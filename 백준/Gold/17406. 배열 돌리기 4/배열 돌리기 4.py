N, M, K = map(int, input().split())
matrix_og = []
for _ in range(N):
    matrix_og.append(list(map(int, input().split())))
def applyRotation(i, j, c):
    vec_i = j - C
    vec_j = i - R
    # print("벡터 기준, i, j", vec_i, vec_j)
    
    if -c <= vec_i and vec_i < c:
        if vec_j == -c:
            return vec_i + 1, vec_j
    if -c < vec_j and vec_j <= c:
        if vec_i == -c:
            return vec_i, vec_j - 1
    if -c < vec_i and vec_i <= c:
        if vec_j == c:
            return vec_i - 1, vec_j 
    if -c <= vec_j and vec_j < c:
        if vec_i == c:
            return vec_i, vec_j + 1

rcs_lst = []
for _ in range(K):
    rcs_lst.append(list(map(int, input().split())))
import itertools
per_lst = list(itertools.permutations(range(K)))
res = float("inf")
for el in per_lst:    
    matrix = []
    for m2 in matrix_og:
        matrix.append(m2.copy())
    for el2 in el:
        cmd = rcs_lst[el2]
        R, C, S = cmd[0], cmd[1], cmd[2]
        
        # R, C 인덱스 기준 처리
        R -= 1
        C -= 1
        centerValue = matrix[R][C]
        temp = [[0 for _ in range(2*S+1)] for _ in range(2*S+1)]
        for s in range(S, 0, -1):
            for i in range(R-s, R+s+1):
                for j in range(C-s, C+s+1):
                    if s > abs(i - R) and s > abs(j - C):
                        continue
                    # print("매트릭스기준 i, j", i, j)
                    # print("떨어진 거리 s", s)
                    ni, nj = applyRotation(i, j, s)
                    # print("변환 후 매트릭스 기준 ni, nj", ni, nj)
                    # print("temp 기준 x, y", S+nj, S+ni)
                    temp[S+nj][S+ni] = matrix[i][j]
                    # print(temp)
        for i in range(2*S+1):
            for j in range(2*S+1):
                matrix[R-S+i][C-S+j] = temp[i][j]
        
        matrix[R][C] = centerValue
        
    for m in matrix:
        res = min(res, sum(m))
print(res)