from collections import deque
N, K = map(int, input().split())

if N > K:
    ans = []
    for k in range(N, K -1, -1): ans.append(k)
    print(N-K)
    print(*ans)
    exit()

queue = deque()
queue.append([N, [N]])

vis = [1e9 for _ in range(2 * K + 1)]
vis[N] = 1

min_path = 1e9
while queue:
    node, history = queue.popleft()
    if node == K:
        if min_path > len(history) - 1:
            min_path = len(history) - 1
            answer = [h for h in history]
    if min_path < len(history): continue
    
    if node - 1 > 0:
        if vis[node - 1] > len(history):
            history.append(node - 1)
            vis[node - 1] = len(history) - 1
            queue.append([node - 1, list(map(int, history))])
            history.pop()
    if node + 1 <= 100000:
        if vis[node + 1] > len(history):
            history.append(node + 1)
            vis[node + 1] = len(history) - 1
            queue.append([node + 1, list(map(int, history))])
            history.pop()
    if node * 2 <= K * 2:
        if vis[node * 2] > len(history):
            history.append(node * 2)
            vis[node * 2] = len(history) - 1
            queue.append([node * 2, list(map(int, history))])
            history.pop()

print(min_path)
print(*answer)