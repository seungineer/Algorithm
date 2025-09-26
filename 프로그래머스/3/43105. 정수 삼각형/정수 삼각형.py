def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j]
    
    for i in range(N-1):
        for j in range(N-1):
            try:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
            except:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
                
    return max(dp[-1])