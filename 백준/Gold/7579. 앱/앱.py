N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
max_costs = sum(costs)
dp = [[0 for _ in range(max_costs + 1)] for _ in range(N+1)]

answer = max_costs
for i in range(1, N+1):
    cost = costs[i]
    byte = memories[i]
    for j in range(max_costs + 1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], byte + dp[i-1][j-cost])
        
        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)