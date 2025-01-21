N = int(input())
seq = list(map(int,input().split()))

dp = [[0 for _ in range(21)] for _ in range(N)]
dp[0][seq[0]] += 1

for i in range(1, N):
    for j in range(21):
        k = dp[i-1][j]
        if k == 0: continue
        if 0 <= j + seq[i] and j + seq[i] <= 20:
            dp[i][j+seq[i]] += k
        if 0 <= j - seq[i] and j - seq[i] <= 20:
            dp[i][j-seq[i]] += k

print(dp[-2][seq[-1]])

    