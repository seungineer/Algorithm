from collections import defaultdict
def solution(genres, plays):
    answer = []
    gCnts = defaultdict(int)
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        gCnts[g] += p
    gCnts = sorted(gCnts.items(), key= lambda x: x[1], reverse = True)
    
    pCnts = defaultdict(set)
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        pCnts[g].add(tuple([p, i]))
    
    for g, c in gCnts:
        lst = sorted(list(pCnts[g]), key= lambda x: [x[0], -1 * x[1]], reverse = True)
        for i in range(len(lst)):
            if i == 2: break
            a, b = lst[i]
            answer.append(b)
            
    return answer