MOD = 9901
N = int(input())

dp = [[0,0,0] for _ in range(N)]
dp[0][0] = 1 # 0자리에 있는 경우
dp[0][1] = 1 # 1자리에 있는 경우
dp[0][2] = 1 # 둘 다 없는 경우

for i in range(1, N):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = sum(dp[i-1]) % MOD

print(sum(dp[-1]) % MOD)