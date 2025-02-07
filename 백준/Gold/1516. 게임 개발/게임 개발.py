from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
times = [ 0 for _ in range(N+1)] # 걸리는 시간
maxTimes = [ 0 for _ in range(N+1)] # 걸리는 시간
preBuilds = [ set() for _ in range(N+1)] # 선행 건물 집합

qu = deque()
graph = dict()
for num in range(1, N+1):
    inputs = list(map(int, input().rstrip().split()))
    times[num] = inputs[0]
    for st in inputs[1:]:
        preBuilds[num].add(st)
        if st in graph: graph[st].append(num)
        else: graph[st] = [num]
    
    preBuilds[num].discard(-1)
    if not preBuilds[num]:
        qu.append((num, times[num]))
        maxTimes[num] = times[num]
        
while qu:
    num, currentTime = qu.popleft()
    if not num in graph: continue
        
    for next_node in graph[num]:
        if not preBuilds[next_node]: continue
            
        preBuilds[next_node].discard(num)
        maxTimes[next_node] = max(maxTimes[next_node], currentTime + times[next_node])
        if not preBuilds[next_node]:
            qu.append((next_node, maxTimes[next_node]))

for i in range(1, N+1): print(maxTimes[i])
    