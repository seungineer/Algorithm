n = int(input())

dp = [[0, 0, 0]for _ in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    if i == 0:
        dp[i][0] = r
        dp[i][1] = g
        dp[i][2] = b
    
        continue
    dp[i][1] = min(dp[i-1][0]+g, dp[i-1][2]+g)
    dp[i][0] = min(dp[i-1][1]+r, dp[i-1][2]+r)
    dp[i][2] = min(dp[i-1][0]+b, dp[i-1][1]+b)
print(min(dp[n-1]))