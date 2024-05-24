n = int(input())
graph = dict()
for i in range(n):
    seq = input().strip()
    cnt = 0
    graph[i] = []
    for k in seq:
        if k == 'Y':
            graph[i].append(cnt)
        cnt += 1

max_res = -1
for i in range(n):
    friend_list = []
    friend_list.append(i)
    for el in graph[i]:
        friend_list.append(el)
        for temp in graph[el]:
            friend_list.append(temp)
    res = len(list(set(friend_list)))
    max_res = max(res, max_res)
print(max_res-1)