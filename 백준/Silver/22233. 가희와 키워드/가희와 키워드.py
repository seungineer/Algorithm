N, M = map(int, input().split())
memo_set = set()
for _ in range(N):
    memo_set.add(input())
for _ in range(M):
    lst = list(map(str, input().split(',')))
    for el in lst:
        if el in memo_set: memo_set.discard(el)
    print(len(memo_set))