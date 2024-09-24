N = int(input())
seq = [(int(input()) - 1) for _ in range(N)]

graph = {}
base_answer = []
for i in range(N):
    graph[i] = seq[i]
    if i == seq[i]: base_answer.append(i)

answer = []
max_len = [set()]
def dfs(node, start):
    vis[node] = 1
    answer.append(node)
    next_node = graph[node]
    if next_node == start:
        for k in answer:
            max_len[0].add(k)
        return
    if vis[next_node] == 0:
        vis[next_node] = 1
        dfs(next_node, start)

for st in range(N):
    if st == seq[st]: continue
    vis = [0 for _ in range(N)]
    dfs(st, st)
    answer.clear()

print(len(max_len[0]) + len(base_answer))
for k in base_answer:
    max_len[0].add(k)
ans = sorted(list(max_len[0]))

for k in ans:
    print(k+1)