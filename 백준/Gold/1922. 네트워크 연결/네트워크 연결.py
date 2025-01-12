def solution():
    N = int(input())
    M = int(input())
    input_lst = [list(map(int, input().split())) for _ in range(M)]
    input_lst.sort(key=lambda x: x[2])
    
    parents = [i for i in range(N+1)]
    ans = 0
    
    def find(child):
        if parents[child] == child:
            return child
        parents[child] = find(parents[child])
        return parents[child]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b: return
        else:  parents[a] = b
    
    for i in range(M):
        a, b, cost = input_lst[i]
        if a == b: continue
        if a < b: a, b= b, a
        if sum(parents) == N: break
        if find(a) == find(b): continue
        ans += cost
        union(a, b)

    print(ans)
    
    return
solution()