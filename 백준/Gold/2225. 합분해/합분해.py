MOD = int(1e9)
N, K = map(int, input().split())
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1, N+1):
    dp[1][i] = 1
for j in range(1, K+1):
    dp[j][1] = j

for i in range(1, K+1):
    for j in range(2, N+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD
print(dp[K][N] % MOD)