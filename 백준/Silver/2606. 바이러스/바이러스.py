N = int(input())
e = int(input())

def findParent(parent_list, V):
    if parent_list[V] != V:
        parent_list[V] = findParent(parent_list, parent_list[V])
        return parent_list[V]
    else:
        return V

def unionAB(x, y):
    a = findParent(parent_list, x)
    b = findParent(parent_list, y)
    if a == b:
        return
    
    if a < b:
        parent_list[b] = a
    else:
        parent_list[a] = b

parent_list = [0 for _ in range(N+1)]
for i in range(1, N+1):
    parent_list[i] = i

for i in range(e):
    a, b = map(int, input().split())
    if findParent(parent_list, a) != findParent(parent_list, b):
        unionAB(a, b)

infected_count = sum(1 for i in range(1, N+1) if findParent(parent_list, i) == 1) - 1
print(infected_count)