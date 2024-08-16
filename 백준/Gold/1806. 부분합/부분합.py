n, s = map(int, input().split())
seq = list(map(int, input().split()))
st = 0
en = 0
tot = seq[0]
isFind = False
min_len = float("inf")
while en < n and st <= en:
    # print(st, en)
    if not isFind:
        if tot >= s:
            isFind = True
            min_len = min(min_len, en - st + 1)
            tot -= seq[st]
            st += 1
        else:
            en += 1
            if en < n:
                tot += seq[en]
    else:
        if tot >= s:
            min_len = min(min_len, en - st + 1)
            tot -= seq[st]
            st += 1
        else:
            tot -= seq[st]
            st += 1
            en += 1
            if en < n:
                tot += seq[en]

if not isFind:
    print(0)
else:
    print(min_len)