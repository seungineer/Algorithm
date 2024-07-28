import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(str, input().split()))

dp = [[0 for _ in range(N)]for _ in range(N)]
for i in range(N-1):
    dp[i][i] = 1
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1
dp[N-1][N-1] = 1
if N > 1:
    for length in range(2, N):
        for i in range(N-length):
            if lst[i] == lst[i+length]:
                if dp[i+1][i+length-1] == 1:
                    dp[i][i+length] = 1
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if dp[a][b] :
        print(1)
    else:
        print(0)
