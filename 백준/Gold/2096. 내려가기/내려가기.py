import sys
input = sys.stdin.readline

n = int(input())
matrix = []

# Only store current and previous rows to reduce memory usage
dp = [[[0,0], [0,0], [0,0]] for _ in range(2)]

for i in range(n):
    matrix.append(list(map(int, input().split())))
    
    # i state is now just the current row index (0 or 1)
    i %= 2

    dp[i][0][0] = max(matrix[0][0]+dp[1-i][0][0], matrix[0][0]+dp[1-i][1][0])
    dp[i][0][1] = min(matrix[0][0]+dp[1-i][0][1], matrix[0][0]+dp[1-i][1][1])

    dp[i][1][0] = max(matrix[0][1]+dp[1-i][0][0], matrix[0][1]+dp[1-i][1][0], matrix[0][1]+dp[1-i][2][0])
    dp[i][1][1] = min(matrix[0][1]+dp[1-i][0][1], matrix[0][1]+dp[1-i][1][1], matrix[0][1]+dp[1-i][2][1])

    dp[i][2][0] = max(matrix[0][2]+dp[1-i][1][0], matrix[0][2]+dp[1-i][2][0])
    dp[i][2][1] = min(matrix[0][2]+dp[1-i][1][1], matrix[0][2]+dp[1-i][2][1])
    matrix.pop()

# Track max and min scores separately
max_score = -1
min_score = float("inf")

for j in range(3):
    max_score = max(max_score, dp[(n-1)%2][j][0])
    min_score = min(min_score, dp[(n-1)%2][j][1])
print(max_score, min_score)