from collections import deque
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    if K == 1:
        print(1, 1)
        continue
    dict = {} # 'alphabet' : [[index, 개수],[index, 개수], ...]
    shortest = float("inf")
    longest = -float("inf")
    for i in range(len(W)):
        s = W[i]
        if s in dict.keys():
            if len(dict[s]) == K-1:
                shortest = min(shortest, i - dict[s][0][0] + 1)
                longest = max(longest, i - dict[s][0][0] + 1)
                dict[s].popleft()    
            dict[s].append([i, len(dict[s])+1])
        else:
            dict[s] = deque()
            dict[s].append([i, 1])


    if shortest != float("inf") and longest != -float("inf"):
        print(shortest, longest)
    else:
        print(-1)