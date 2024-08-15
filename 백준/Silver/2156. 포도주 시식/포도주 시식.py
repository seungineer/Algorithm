n = int(input())
seq = [-float("inf")]
for _ in range(n):
    seq.append(int(input()))
if n <= 2:
    if n == 1:
        print(seq[1])
    else:
        print(seq[1]+seq[2])
    exit()

dp = [[0,0,0,0] for _ in range(n+1)]
dp[3][0] = seq[2] + seq[3] # x o o
dp[3][1] = max(seq[1] + seq[3], seq[3]) # o x o / x x o
dp[3][2] = max(seq[1] + seq[2], seq[2]) # o o x / x o x
dp[3][3] = seq[1] # o x x

for i in range(4, n+1):
    dp[i][0] = dp[i-1][1] + seq[i]
    dp[i][1] = max(dp[i-1][2] + seq[i], dp[i-1][3] + seq[i])
    dp[i][2] = max(dp[i-1][0], dp[i-1][1])
    dp[i][3] = dp[i-1][2]
print(max(dp[-1]))
