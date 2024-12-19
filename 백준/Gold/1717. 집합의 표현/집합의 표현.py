import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
parents = [i for i in range(N+1)]

def find_parent(node):
    next_node = node
    if parents[node] != node:
        next_node = find_parent(parents[node])
        parents[node] = next_node
    return next_node

def fix_parent(node, target):
    next_node = node
    if parents[node] != node:
        next_node = fix_parent(parents[node], target)
        parents[node] = next_node
    else:
        parents[node] = target
    return next_node

for _ in range(M):
    command, a, b = map(int, input().rstrip().split())
    
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    
    if command == 0:
        if parent_a > parent_b:
            fix_parent(a, min(parent_a, parent_b))
        else:
            fix_parent(b, min(parent_a, parent_b))
        
    else:
        if parent_a == parent_b: print("YES")
        else: print("NO")
