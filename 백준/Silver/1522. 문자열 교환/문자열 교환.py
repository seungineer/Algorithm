# b의 개수 만큼 범위로 슬라이딩 윈도우 해서
# a가 가장 적게 포함된 것이 정답(최솟값)
seq = list(map(str, input()))

b_cnt = seq.count('b')

for i in range(b_cnt):
    seq.append(seq[i])
st = 0
en = b_cnt - 1
min_a = float("inf")
while en < len(seq):
    a_cnt = 0
    for i in range(st, en + 1):
        if seq[i] == 'a':
            a_cnt += 1
    min_a = min(min_a, a_cnt)
    st += 1
    en += 1
print(min_a)