N, C = map(int, input().split())
M = int(input())
info = []
for _ in range(M):
    st, en, w = map(int, input().split())
    info.append([en-st-1, -w, st])
info.sort()
boxCount = [C for _ in range(N+1)]
answer = 0
while info:
    diff, minus_weight, start = info.pop(0)
    weight = - minus_weight

    affordWeight = min(boxCount[start:start + diff + 1])
    if affordWeight < weight: weight = affordWeight
    if weight != 0:
        answer += weight
        for i in range(start, start + diff + 1):
            boxCount[i] -= weight
        
print(answer)