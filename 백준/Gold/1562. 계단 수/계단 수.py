def solution():
    MOD = int(1e9)
    N = int(input())
    cols = [[dict() for _ in range(10)] for _ in range(2)]
    
    for i in range(N):
        if i == 0:
            for k in range(1,10):
                new_set = set()
                new_set.add(k)
                cols[0][k][tuple(new_set)] = 1
            continue
        else:
            for k in range(10): # 이전 숫자
                for ex_set in cols[0][k].keys():              
                    new_set = set(ex_set)
                    if k - 1 >= 0:
                        new_set.add(k-1)
                        if tuple(new_set) in cols[1][k-1]: cols[1][k-1][tuple(new_set)] += cols[0][k][tuple(ex_set)] % MOD
                        else: cols[1][k-1][tuple(new_set)] = cols[0][k][tuple(ex_set)] % MOD
                        cols[1][k-1][tuple(new_set)] %= MOD
                    
                    new_set = set(ex_set)
                    if k + 1 <= 9:
                        new_set.add(k+1)
                        if tuple(new_set) in cols[1][k+1]: cols[1][k+1][tuple(new_set)] += cols[0][k][tuple(ex_set)] % MOD
                        else: cols[1][k+1][tuple(new_set)] = cols[0][k][tuple(ex_set)] % MOD
                        cols[1][k+1][tuple(new_set)] %= MOD
                    
        # 2열을 1열로 복사
        for num in range(10):
            # 1열 초기화
            cols[0][num] = dict()
            for new_set in cols[1][num].keys():
                cols[0][num][tuple(new_set)] = int(cols[1][num][tuple(new_set)])
            # 2열 초기화
            cols[1][num] = dict()
    ans = 0
    for k in range(10):
        for el in cols[0][k].keys():
            if len(el) == 10:
                ans += cols[0][k][tuple(el)] % MOD
    
    print(ans % MOD)
    
    return
solution()