n = int(input())
lst = list(map(int,input().split()))
st = 0
en = len(lst)-1
min_tot = float("inf")

while st < en:
    tot = abs(lst[en] + lst[st])
    if min_tot > tot:
        res_st = st
        res_en = en
        min_tot = min(min_tot, tot)
    if lst[en] * lst[st] > 0: #부호가 같으면
        if lst[en] > 0:
            en -= 1
        else:
            st += 1
    else: #부호가 다르면
        if lst[en] > abs(lst[st]):
            en -= 1
        else:
            st += 1
print(lst[res_st], lst[res_en])