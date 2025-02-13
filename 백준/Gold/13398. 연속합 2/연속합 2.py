def solution():
    N = int(input())
    seq = list(map(int, input().split()))
    
    dp = [[k, k] for k in seq]
    maxSum = seq[0]
    
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0] + seq[i], dp[i][0])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + seq[i])
        maxSum = max(maxSum, dp[i][0], dp[i][1])
    print(maxSum)
            
    return
solution()