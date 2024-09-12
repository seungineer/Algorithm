from collections import deque
N, D, K, C = map(int, input().split())

qu = []
kind = set()
for _ in range(N):    
    qu.append(int(input()))
max_cnt = -float("inf")
for st in range(N):
    for i in range(st, st+K):
        target = qu[i]
        kind.add(target)
        if i == st : qu.append(target)
    if C in kind:
        max_cnt = max(max_cnt, len(kind))
    else:
        max_cnt = max(max_cnt, len(kind)+1)
    kind.clear()
print(max_cnt)
