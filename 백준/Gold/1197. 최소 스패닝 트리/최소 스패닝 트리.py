import sys
read = sys.stdin.readline

v, e = map(int, read().split())
parent_lst = [0] * (v+1)
for i in range(1, v+1): # 각 노드의 parent list 생성
    parent_lst[i] = i

def findParent(parent_lst, x): # parent list에서 x의 부모 노드 찾기
    if parent_lst[x] != x: # 부모 노드 = 자식 노드인 경우
        parent_lst[x] = findParent(parent_lst, parent_lst[x]) # 부모 노드 != 자식 노드인 경우, 부모 노드가 찐 부모 노드인지 확인하러 감
    return parent_lst[x]

def unionAB(parent_lst, x, y): # x, y를 합집합으로(=하나의 공통된 부모 노드를 갖도록) 연결하는 것 
    a = findParent(parent_lst, x)
    b = findParent(parent_lst, y)
    if a < b:
        parent_lst[b] = a
    else:
        parent_lst[a] = b

edges = []
tot = 0

for _ in range(e):
    a, b, cost = map(int, read().split())
    edges.append((cost, a, b))

edges.sort() # cost 기준으로 오름차순 sorting

for i in range(e):
    cost, a, b = edges[i]

    if findParent(parent_lst, a) != findParent(parent_lst, b) :
        unionAB(parent_lst, a, b)
        tot += cost

print(tot)

