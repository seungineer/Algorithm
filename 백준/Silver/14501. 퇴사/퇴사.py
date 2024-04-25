import sys
sys. setrecursionlimit(10**6)

n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))
max_compensate = [0]

def calculate(i, compensate):
    if i > n-1:
        if max(max_compensate) < compensate:
            max_compensate.append(compensate)
        return 
    
    compensate += table[i][1]
    period = table[i][0]

    if i+period <= n:
        calculate(i+period, compensate)
    compensate -= table[i][1]
    calculate(i+1, compensate)
    

for start in range(n):
    compensate = 0
    calculate(start, compensate)
print(max(max_compensate))
    
