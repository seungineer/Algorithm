def solution(M):
    # arr에는 작은 값, 큰 값 순으로 숫자 변환하여 담기
    names = dict()
    num = 1
    arr = []
    for _ in range(M):
        name1, name2 = input().split()
        a, b = 0, 0
        if name1 in names: a = names[name1]
        else: 
            names[name1] = num
            a = num
            num += 1
        if name2 in names: b = names[name2]
        else: 
            names[name2] = num
            b = num
            num += 1
        if a > b: a, b = b, a
        arr.append([a, b])
    
    N = num
    parents = [i for i in range(N+1)]
    counts = [1 for _ in range(N+1)]
    def find(node):
        if parents[node] == node:
            return node
        parents[node] = find(parents[node])
        return parents[node]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parents[b] = a
            aCnt = counts[a]
            bCnt = counts[b]
            counts[a] += bCnt
            counts[b] += aCnt
    
    for a, b in arr:
        a = find(a)
        b = find(b)
        union(a, b)
        print(counts[a])
    return
TC = int(input())
for _ in range(TC):
    M = int(input())
    solution(M)