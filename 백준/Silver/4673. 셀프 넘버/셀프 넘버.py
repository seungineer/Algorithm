selfNum = [True for _ in range(10001)]

def d(num):
    str_num = str(num)
    tot = num
    for s in str_num:
        tot += int(s)
    return tot

for i in range(1, 10001):
    if selfNum[i] :
        res = i
    else:
        continue
    while res <= 10000:
        res = d(res)
        if res <= 10000:
            selfNum[res] = False
for i in range(1, 10001):
    if selfNum[i]:
        print(i)