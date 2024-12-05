N = int(input())
seq = list(map(int, input().split()))
cut_node = int(input())

down_nodes = dict()
for i in range(N):
    parent = seq[i]
    if parent == -1:
        root = i
        continue
    if parent in down_nodes: down_nodes[parent].append(i)
    else: down_nodes[parent] = [i]

if root == cut_node:
    print(0)
    exit()

answer = [0]
def dfs(node):
    for down in down_nodes[node]:
        if down == cut_node:
            if len(down_nodes[node]) == 1: answer[0] += 1
            continue
        
        if down in down_nodes: dfs(down)
        else: answer[0] += 1

dfs(root)
print(answer[0])