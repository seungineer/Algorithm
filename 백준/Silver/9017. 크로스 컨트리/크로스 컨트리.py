T = int(input())
for _ in range(T):
    N = int(input())
    seq = list(map(int, input().split()))

    delete_set = set()
    cnt_dict = {}
    max_team = -float("inf")
    for s in seq:
        max_team = max(max_team, s)
        delete_set.add(s)
        if s in cnt_dict.keys():
            cnt_dict[s] += 1
        else:
            cnt_dict[s] = 1
        if cnt_dict[s] == 6:
            delete_set.discard(s)
    score_lst = [[] for _ in range(max_team+1)]
    score = 1
    min_score = float("inf")
    for i in range(N):
        if seq[i] in delete_set:
            continue
        
        score_lst[seq[i]].append(score)
        
        if len(score_lst[seq[i]]) == 5:
            if min_score > sum(score_lst[seq[i]][:4]):
                min_score = sum(score_lst[seq[i]][:4])
                team = seq[i]
            elif min_score == sum(score_lst[seq[i]][:4]):
                if score_lst[team][4] > score_lst[seq[i]][4]:
                    min_score = sum(score_lst[seq[i]][:4])
                    team = seq[i]

        score += 1
    print(team)