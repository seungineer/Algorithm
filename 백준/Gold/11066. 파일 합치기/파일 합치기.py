def solution():
    N = int(input())
    seq = [0] + list(map(int, input().split()))
    prefixes = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        prefixes[i] = prefixes[i-1] + seq[i]
 
    DP = [[0 for i in range(N+1)] for _ in range(N+1)]
    for i in range(2, N+1):
        for j in range(1, N+2-i):
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (prefixes[j+i-1] - prefixes[j-1])
 
    print(DP[1][N])
 
for _ in range(int(input())):
    solution()
