# 가장 끝자리가 0 -> 뒤가       1
# 가장 끝자리가 1 -> 뒤가 0 또는 2
# 가장 끝자리가 2 -> 뒤가 1 또는 3
# ...
# 가장 끝자리가 8 -> 뒤가 7 또는 9
# 가장 끝자리가 9 -> 뒤가 8

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]
for i in range(1,10): dp[0][i] = 1
for i in range(1, N):
    for j in range(10):
        if 0 <= j - 1: dp[i][j] += dp[i-1][j-1]
        if j + 1 < 10: dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= 10**9

print(sum(dp[-1])%10**9)