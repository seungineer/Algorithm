N = int(input())
matrices = []
for _ in range(N):
    r, c = map(int, input().split())
    matrices.append([r, c])
dp = [[0 for _ in range(N)] for _ in range(N)]

for diff in range(N - 1):
    for i in range(N - 1 - diff):
        j = i + diff + 1
        dp[i][j] = float("inf")
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1])

print(dp[0][-1])
