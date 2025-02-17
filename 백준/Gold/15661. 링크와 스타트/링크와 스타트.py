def solution():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    def calAddScore(org, p):
        s = 0
        if p in org: return s

        for mate in list(org):
            s += matrix[p][mate] + matrix[mate][p]
        return s

    counter = set()
    for i in range(N):
        counter.add(i)
    scores = dict()

    def bt(mine, opposer, idx, score):
        
        if len(mine) >= 1 and len(opposer) >= 1:
            tupleMines = tuple(sorted(mine))
            tupleOpposers = tuple(sorted(opposer))
            if not tupleMines in scores:
                scores[tupleMines] = score
            if tupleMines in scores and tupleOpposers in scores:
                ans[0] = min(ans[0], abs(scores[tupleMines] - scores[tupleOpposers]))
        for player in range(idx+1, N):
            additional = calAddScore(mine, player)
            opposer.discard(player)
            mine.add(player)
            scores[tuple(sorted(mine))] = score + additional
            bt(mine, opposer, player, score + additional)
            mine.discard(player)
            opposer.add(player)
      
    ans = [int(1e10)]
    for player in range(N):
        counter.discard(player)
        myTeam = set()
        myTeam.add(player)
        scores[tuple(myTeam)] = 0
        bt(myTeam, counter, player, 0) # 나의 팀, 상대 팀, 현재 반영 플레이어, 현재 점수
        counter.add(player)
    print(ans[0])
solution()