def solution():
    MOD = int(1e9) + 9
    N = 100000
    dp = [[0,0,0] for _ in range(N+1)]
    dp[1][0] = 1
    dp[2][1] = 1
    dp[3][0] = 1
    dp[3][1] = 1
    dp[3][2] = 1
    for i in range(4, N+1):
        dp[i][0] = (sum(dp[i-1]) - dp[i-1][0]) % MOD
        dp[i][1] = (sum(dp[i-2]) - dp[i-2][1]) % MOD
        dp[i][2] = (sum(dp[i-3]) - dp[i-3][2]) % MOD
    TC = int(input())
    for _ in range(TC):
        n = int(input())
        print(sum(dp[n]) % MOD)
    
solution()