N = int(input())
seq = []
for _ in range(N):
    st, en = map(int, input().split())
    seq.append([st, 1])
    seq.append([en, -1])
seq.sort()

max_cnt = -1
cnt = 0
info = dict()
for i in range(2*N):
    line, point = seq[i]
    cnt += point
    info[line] = cnt
    if max_cnt < cnt:
        max_cnt = cnt
        te = line
        continue
    if max_cnt > cnt:
        tx = line

print(max_cnt)

te = -1
for key in info:
    if te == -1 and info[key] == max_cnt:
        te = key
        continue
    if te != -1 and info[key] != max_cnt:
        tx = key
        break
print(te, tx)
