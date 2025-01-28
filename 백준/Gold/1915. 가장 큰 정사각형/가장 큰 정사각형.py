import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().rstrip().split())
    matrix = [list(map(int, input().rstrip())) for _ in range(N)]
    dp = [[0 for _ in range(M)] for _ in range(N)]
    maxArea = 0
    for i in range(N):
        for j in range(M):
            if i == 0:
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    maxArea = 1
            else:
                if j == 0:
                    if matrix[i][j] == 1:
                        dp[i][j] = 1
                        maxArea = 1
    
    def sizeCal(l, x, y):
        for length in range(1, l+1):
            if matrix[x][y-length] != 1 or matrix[x-length][y] != 1:
                return length
        return l+1
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                if i - 1 >= 0 and j - 1 >= 0:
                    targetSize = dp[i-1][j-1]
                    if targetSize == 0:
                        dp[i][j] = 1
                        continue
                    size = sizeCal(targetSize, i, j)
                    dp[i][j] = size
                    maxArea = max(maxArea, size**2)              
    print(maxArea)
solution()