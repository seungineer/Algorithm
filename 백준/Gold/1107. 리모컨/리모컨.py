target = int(input())
M = int(input())
if M != 0: disable= list(map(int, input().split()))
else: disable = []

min_cnt = [abs(target - 100)]

def makeStringNumber(stringNum):
    if len(stringNum) > 6: return
    min_cnt[0] = min(min_cnt[0] ,len(stringNum) + abs(int(stringNum) - target))

    for j in range(10):
        if j in disable: continue
        stringNum += str(j)
        makeStringNumber(stringNum)
        stringNum = stringNum[:-1]

for i in range(10):
    if i in disable: continue
    stringNum = str(i)
    makeStringNumber(stringNum)
print(min_cnt[0])