def solution():
    C,N = map(int,input().split())
    cost_list = [list(map(int,input().split())) for _ in range(N)]
    dp = [int(1e9) for _ in range(C+100)]
    dp[0]=0

    for cost, p in cost_list:
        for j in range(p,C+100):
            dp[j] = min(dp[j-p]+cost,dp[j])

    print(min(dp[C:]))
solution()