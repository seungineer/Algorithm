N, M = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()

output_set = set()

def dfs(ans):
    if len(ans) == M:
        if tuple(ans) in output_set: return
        output_set.add(tuple(ans))
        print(*ans)
        return
    
    for next_idx in range(N):
        ans.append(seq[next_idx])
        dfs(ans)
        ans.pop()

for i in range(N):
    dfs([seq[i]])
