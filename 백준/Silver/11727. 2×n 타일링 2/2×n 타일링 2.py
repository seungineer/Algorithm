n = int(input())
dp = [0 for _ in range(n+1)] # i일 때 최대로 채울 수 있는 방법의 수
dp[0] = 1
dp[1] = 1
if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        dp[i] = (dp[i-1])%10007 + (2*dp[i-2])%10007
    print(dp[n]%10007)