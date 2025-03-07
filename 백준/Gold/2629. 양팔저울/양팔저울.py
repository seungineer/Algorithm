def solution():
    N = int(input())
    weights = list(map(int, input().split()))
    M = int(input())
    seq = list(map(int, input().split()))

    # 각 추를 활용해서 만들어 낼 수 있는 수의 경우를 찾는 것
    # 안 쓰이든지, 구슬 편이든지, 구슬 반대편이든지
    # Knapsack P 처럼
    MAXWEIGHT = 15000
    dp = [[False for _ in range(MAXWEIGHT+1)] for _ in range(N)]
    dp[0][weights[0]] = True
    dp[0][0] = True
    for idx in range(1, N):
        for j in range(MAXWEIGHT + 1):
            if dp[idx-1][j]:
                dp[idx][j] = True
                dp[idx][abs(j-weights[idx])] = True
                if j+weights[idx] < MAXWEIGHT+1:
                    dp[idx][j+weights[idx]] = True
    ans = []
    for el in seq:
        if el > MAXWEIGHT:
            ans.append("N")
            continue
        
        if dp[N-1][el]:
            ans.append("Y")
        else:
            ans.append("N")
    print(*ans)



solution()