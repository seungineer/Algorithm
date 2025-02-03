import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
preworkCnt = [0 for _ in range(N+1)]
doneCnt = [0 for _ in range(N+1)]
runningtimes = [0 for _ in range(N+1)]
maxRunningtimes = [0 for _ in range(N+1)]
graph = dict()
qu = deque()
for en in range(1, N+1):
    inputs = list(map(int, input().rstrip().split()))
    time, cnt = inputs[0], inputs[1]
    runningtimes[en] = time
    preworkCnt[en] = cnt
    if cnt == 0:
        qu.append((en, time)) # (node, 현재 노드까지 최대 시간)
    for st in inputs[2:]:
        if st in graph: graph[st].append(en)
        else: graph[st] = [en]

ans = -1
while qu:
    node, currentTime = qu.popleft()
    ans = max(ans, currentTime)
    if not node in graph: continue
    for nextNode in graph[node]:
        doneCnt[nextNode] += 1
        maxRunningtimes[nextNode] = max(maxRunningtimes[nextNode], currentTime + runningtimes[nextNode])
        if doneCnt[nextNode] == preworkCnt[nextNode]:
            qu.append((nextNode, maxRunningtimes[nextNode]))

print(ans)
