import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
seq = [int(input()) for _ in range(P)]

parents = [i for i in range(G+1)]

def find(node):
    if parents[node] == node:
        return node
    parent = find(parents[node])
    parents[node] = parent
    return parent

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a
cnt = 0
for gate in seq:
    parentGate = find(gate)
    if parentGate == 0: break
    union(parentGate-1, parentGate)
    cnt += 1

print(cnt)