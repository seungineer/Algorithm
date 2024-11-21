N, C = map(int, input().split())
M = int(input())
info = []
for _ in range(M):
    st, en, w = map(int, input().split())
    info.append([en, -w, st])
info.sort()
boxCount = [C for _ in range(N+1)]
answer = 0
for j in range(M):
    affordWeight = 1e9
    end, minus_weight, start = info[j]
    weight = - minus_weight
    for k in range(start, end):
        affordWeight = min(affordWeight, boxCount[k])
    
    if affordWeight < weight: weight = affordWeight
    if weight != 0:
        answer += weight
        for i in range(start, end):
            boxCount[i] -= weight
        
print(answer)