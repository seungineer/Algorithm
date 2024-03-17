import sys

read = sys.stdin.readline
N = 2
data = [list(map(int, read().split())) for _ in range(N)]

n = data[0][0]
target = data[0][1]
lst = data[1]
# flag = False
max_tot = 0
#로직
lst.sort(reverse=False)

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = (lst[i] + lst[j] + lst[k])
                
            if target >= total:
                max_tot = max(max_tot, total)
                
print(max_tot)