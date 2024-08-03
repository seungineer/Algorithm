n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)] # ㅡ,ㅣ,대각 형태일 때, 경로 수
dp[0][1] = [1,0,0]
n -= 1
for pointsum in range(2, 2*n+1):
    for i in range(pointsum+1):
        j = pointsum - i
        if n < i or n < j:
            continue
        if matrix[i][j] == 1: # 가려고 하는 곳이 1이 아님
            continue
        # ㅡ 형태 파이프 추가 시 경우의 수
        ## 직전 ㅡ, 직전 비탈 케이스
        dp[i][j][0] = (dp[i][j-1][0]) + (dp[i][j-1][2])
        # ㅣ 형태 파이프 추가 시 경우의 수
        ## 직전 ㅣ, 직전 비탈 케이스
        dp[i][j][1] = (dp[i-1][j][1]) + (dp[i-1][j][2])
        #  비탈 형태 파이프 추가 시 경우의 수
        if matrix[i-1][j] != 1 and matrix[i][j-1] != 1:
            dp[i][j][2] = sum(dp[i-1][j-1])

print(sum(dp[n][n]))