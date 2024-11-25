import sys
input = sys.stdin.readline
N, B = map(int, input().split())
matrixOrg = []
for _ in range(N):
    temp_lst = list(map(int, input().split()))
    matrixOrg.append(temp_lst)

def multiplyMatrix(matrixA, matrixB):
    answer = []
    for i in range(N):
        answer.append([])
        for j in range(N):
            tot = 0
            for k in range(N):
                tot += (matrixA[i][k] % 1000) * (matrixB[k][j] % 1000)
            answer[i].append(tot % 1000)
    return answer


def divideConquer(n, matrixOrg):
    if n <= 1: return matrixOrg
    
    if n % 2 == 1:
        subRes = divideConquer(n//2, matrixOrg)
        subRes = multiplyMatrix(subRes, subRes)
        return multiplyMatrix(subRes, matrixOrg)
    
    subRes = divideConquer(n//2, matrixOrg)
    return multiplyMatrix(subRes, subRes)

isOdd = B % 2

if isOdd:
    ans = divideConquer(B-1, matrixOrg)
    if B != 1:
        ans = multiplyMatrix(ans, matrixOrg)
else:
    ans = divideConquer(B, matrixOrg)

def supplier(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] %= 1000
    
    return matrix

supplier(ans)

for el in ans:
    print(*el)
    