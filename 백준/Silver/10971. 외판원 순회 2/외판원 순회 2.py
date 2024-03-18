from itertools import permutations
import sys

read = sys.stdin.readline
n = int(read())
w = [list(map(int, read().split())) for _ in range(n)]

#로직
perms =  permutations(range(n))
maxsize = sys.maxsize


for p in perms:
    flag = True
    cost = 0
    if w[p[-1]][p[0]] == 0: 
        continue # 순열에서 마지막 방문 도시 to 시작 도시 복귀 불가능한 경우
    
    for i in range(n-1):
        from_v = p[i]
        to_v = p[i+1]
        if w[from_v][to_v] == 0: # from -> to 불가능한 경우 제외
            flag = False
            break

        cost += w[from_v][to_v]

        if cost > maxsize: # 최소 비용보다 더 커지는 경우 제외
            flag = False
            break
  
    if flag == True:
        cost += w[p[-1]][p[0]]
        maxsize = min(maxsize, cost)
        
        
print(maxsize)