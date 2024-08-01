N=int(input())
costs=[list(map(int,input().split())) for _ in range(N)]
ans=float("inf")
for i in range(3):
    dp = [[float("inf"),float("inf"),float("inf")] for _ in range(N)]
    dp[0][i] = costs[0][i]
    for j in range(1,N):
        dp[j][0] = costs[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = costs[j][1] + min(dp[j-1][0],dp[j-1][2])
        dp[j][2] = costs[j][2] + min(dp[j-1][0],dp[j-1][1])
    for k in range(3):
        if i != k:
            ans=min(ans,dp[-1][k])
print(ans)