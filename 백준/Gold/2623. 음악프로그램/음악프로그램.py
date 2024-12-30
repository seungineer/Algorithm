N, M = map(int, input().split())
graph = {}
points = [0 for _ in range(N+1)]
for _ in range(M):
    input_lst = list(map(int, input().split()))
    seq_len = input_lst[0]
    seq = input_lst[1:]
    for i in range(seq_len-1):
        a, b = seq[i], seq[i+1]
        if a in graph:
            if not b in graph[a]:
                graph[a].append(b)
                points[b] += 1
        else:
            graph[a] = [b]
            points[b] += 1

def dfs(node, res):
    if node in graph:
        for pointing_node in graph[node]:
            points[pointing_node] -= 1
    
    for next_node in range(1, N+1):
        if points[next_node] == 0 and not next_node in res and not next_node in ans:
            res.append(next_node)
            dfs(next_node, res)
            break
    
    return res

ans = []
for node in range(1, N+1):
    if points[node] == 0 and not node in ans:
        res = dfs(node, [node])
        for el in res: ans.append(el)

if len(ans) == N:
    for el in ans: print(el)
else: print(0)
