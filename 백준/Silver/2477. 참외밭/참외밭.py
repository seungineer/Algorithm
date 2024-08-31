k = int(input())
seq = []
for _ in range(6):
    seq.append(list(map(int, input().split()))) # [[4, 50]]

# 남, 북 이동에서 가장 긴 변
# 동, 서 이동에서 가장 긴 변
# 같은 방향으로 이동할 때, 그 길이와 사이의 길이

# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
max_len_sn = -1
max_len_ew = -1
cnt_e = 0
cnt_w = 0
cnt_s = 0
cnt_n = 0
for s in seq:
    if s[0] == 1 or s[0] == 2:
        max_len_ew = max(max_len_ew, s[1])
        if s[0] == 1:
            cnt_e += 1
        else:
            cnt_w += 1
    else:
        max_len_sn = max(max_len_sn, s[1])
        if s[0] == 3:
            cnt_s += 1
        else:
            cnt_n += 1
rect_area = max_len_ew * max_len_sn

# seq 정렬
i = 0
while True:
    s = seq[i]
    if s[0] == 1:
        if cnt_e == 2:
            seq.remove(s)
            seq.append(s)
        else:
            break
    elif s[0] == 2:
        if cnt_w == 2:
            seq.remove(s)
            seq.append(s)
        else:
            break
    elif s[0] == 3:
        if cnt_s == 2:
            seq.remove(s)
            seq.append(s)
        else:
            break
    else:
        if cnt_n == 2:
            seq.remove(s)
            seq.append(s)
        else:
            break

lst_ew = []
lst_ns = []
for s in seq:
    if s[0] == 1:
        if cnt_e == 2:
            lst_ew.append(s[1])
    elif s[0] == 2:
        if cnt_w == 2:
            lst_ew.append(s[1])
    elif s[0] == 3:
        if cnt_s == 2:
            lst_ns.append(s[1])
    else:
        if cnt_n == 2:
            lst_ns.append(s[1])
if cnt_e == 2:
    if cnt_n == 2:
        sub_area = lst_ew[1] * lst_ns[0]
    else:
        sub_area = lst_ew[0] * lst_ns[1]
else:
    if cnt_n == 2:
        sub_area = lst_ew[0] * lst_ns[1]
    else:
        sub_area = lst_ew[1] * lst_ns[0]
print((rect_area-sub_area)*k)