N = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(N)]
ans = 1
for j in range(N):
    for i in range(j):
        if seq[i] < seq[j]:
            dp[j] = max(dp[j], dp[i] + 1)
            ans = max(ans, dp[j])

print(ans)
