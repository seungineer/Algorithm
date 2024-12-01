N, M = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()

output_set = set()

def dfs(index, ans):
    if len(ans) == M:
        if tuple(ans) in output_set: return
        output_set.add(tuple(ans))
        print(*ans)
        return
    
    for next_idx in range(index + 1, N):
        ans.append(seq[next_idx])
        dfs(next_idx, ans)
        ans.pop()

for i in range(N - M + 1):
    dfs(i, [seq[i]])
