N = int(input())
matrix = [list(map(float, input().split())) for _ in range(N)]
stars = []
for i in range(N):
    for j in range(i+1, N):
        a, b = matrix[i]
        c, d = matrix[j]
        distance = ((a-c)**2 + (b-d)**2)**(0.5)
        stars.append((i, j, distance))
stars.sort(key= lambda x: x[2])

def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(en, st):
    p_en = find(en)
    p_st = find(st)
    # en < st
    if p_en != p_st:
        parents[p_st] = p_en

parents = [i for i in range(N)]
ans = 0
for k in range(len(stars)):
    en, st, dist = stars[k]
    p_en = find(en)
    p_st = find(st)
    if p_en == p_st: continue
    union(en, st)
    ans += dist
    if sum(parents) == 0: break
print(ans)