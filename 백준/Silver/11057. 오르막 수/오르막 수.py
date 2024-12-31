MOD = 10007
N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N)]
for j in range(10): dp[0][j] = 1

# n자리에서 n-1의 숫자와 같거나 작은 영역에 += 1
for i in range(1, N):
    for val in range(10):
        for k in range(val+1):
            dp[i][val] += dp[i-1][k]
        dp[i][val] %= MOD

print(sum(dp[-1]) % MOD)