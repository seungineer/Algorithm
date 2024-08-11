n = int(input())
lst = list(map(int,input().split()))

if n == 1:
    print(lst[0])
else:
    # lst를 돌면서 음수가 오면
    ## 이전 값까지 더한 게 음수이면 이때까지의 값이 최대인지 검사하고,
    ### 0 에서 다시 시작
    isInit = False
    
    if lst[0] > 0 :
        max_sum = lst[0]
        dp = lst[0]
    else:
        max_sum = lst[0]
        dp = 0
        isInit = True

    for i in range(1, n):
        if lst[i] < 0:
            if not isInit:
                max_sum = max(max_sum, dp)
            else:
                isInit = False
            if dp + lst[i] >= 0:
                max_sum = max(max_sum, dp)
                dp += lst[i]
                max_sum = max(max_sum, dp)
            else:
                dp += lst[i]
                max_sum = max(max_sum, dp)
                dp = 0
                isInit = True
        else:
            max_sum = max(max_sum, dp)
            dp += lst[i]
            isInit = False
    if not isInit:
        max_sum = max(max_sum, dp)
    print(max_sum)
