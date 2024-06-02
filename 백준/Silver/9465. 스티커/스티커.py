t = int(input())

for _ in range(t):
    n = int(input())
    matrix = []
    for _ in range(2):
        matrix.append(list(map(int, input().split())))
    # 이전 선택한 스티커의 위치에 따라 현재 선택할 수 있는 스티커가 달라진다.
    dp = [[0 for _ in range(n)] for _ in range(2)] # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    dp[0][0] = matrix[0][0]
    dp[1][0] = matrix[1][0]
    if n == 1:
        print(max(dp[0][-1], dp[1][-1]))
        continue
    dp[0][1] = dp[1][0] + matrix[0][1]
    dp[1][1] = dp[0][0] + matrix[1][1]
    
    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(matrix[i][j] + dp[1][j-1], matrix[i][j] + dp[0][j-2], matrix[i][j] + dp[1][j-2])
            else:
                dp[i][j] = max(matrix[i][j] + dp[0][j-1], matrix[i][j] + dp[0][j-2], matrix[i][j] + dp[1][j-2])
    print(max(dp[0][-1], dp[1][-1]))