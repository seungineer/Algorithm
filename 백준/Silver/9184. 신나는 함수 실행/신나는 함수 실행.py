
dp = [[[0 for _ in range(20+1)] for _ in range(20+1)] for _ in range(20+1)]

for i in range(20+1):
    for j in range(20+1):
        dp[0][i][j] = 1
for i in range(20+1):
    for j in range(20+1):
        dp[i][0][j] = 1
for i in range(20+1):
    for j in range(20+1):
        dp[i][j][0] = 1

for a in range(1, 20+1):
    for b in range(1, 20+1):
        for c in range(1, 20+1):
            if a < b and b < c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b==-1 and c==-1:
        break
    if a <= 0 or b<= 0 or c<= 0:
        print(f"w({a}, {b}, {c}) =", end=' ')
        print(1)
        continue
    if a>20 or b>20 or c>20:
        print(f"w({a}, {b}, {c}) =", end=' ')
        print(dp[20][20][20])
        continue
    print(f"w({a}, {b}, {c}) =", end=' ')
    print(dp[a][b][c])