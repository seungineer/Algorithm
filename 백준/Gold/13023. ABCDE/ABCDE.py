N, M = map(int, input().split())
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

isPossible = [False]
def dfs(num):
    if len(set_alloc) == 5:
        isPossible[0] = True
        return
    for friend in friends[num]:
        if not friend in set_alloc:
            set_alloc.add(friend)
            dfs(friend)
            set_alloc.discard(friend)
    

set_alloc = set()
for num in range(N):
    set_alloc.add(num)
    dfs(num)
    set_alloc.discard(num)
    if isPossible[0]: break
if isPossible[0]: print(1)
else: print(0)