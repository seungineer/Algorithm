# M번 보다 적게 인출하면서 10^5 개를 만족하면 됨
N, M = map(int, input().split())
spends = [int(input()) for _ in range(N)]

def checkOK(getMoney):
    pocket = 0
    getCnt = 0
    isPossible = True
    for i in range(N):
        spend = spends[i]
        if pocket < spend:
            getCnt += 1
            pocket = getMoney
        pocket -= spend
        
        if getCnt == M + 1 or pocket < 0:
            isPossible = False
            break

    return isPossible

l = min(spends)
r = sum(spends)

while l <= r:
    mid = (l + r) // 2
    if checkOK(mid):
        answer = mid
        r = mid - 1
    else:
        l = mid + 1

print(answer)