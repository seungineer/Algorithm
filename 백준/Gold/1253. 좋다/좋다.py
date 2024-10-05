# N개의 수에서 두개의 합으로 나타낼 수 있는 숫자의 개수
# N*N / 2 = 2 * 10^6 이 모든 경우에 대해서 set를 생성하고,
# 생성한 set에 몇 개나 포함되는지 보면 쉬울 거 같은디..
from itertools import combinations
N = int(input())
comb = list(combinations(range(N), 2))
seq = list(map(int, input().split()))
# seq 내 숫자 종류 빈도 count
dict = {}
for s in seq:
    if s in dict: dict[s] += 1
    else: dict[s] = 1

res_set = set()
for com in comb:
    idx1, idx2 = com[0], com[1]
    # 0과 빈도가 1인 값은 add 하지 않는 처리
    if seq[idx1] == 0:
        if dict[seq[idx2]] == 1: continue
    if seq[idx2] == 0:
        if dict[seq[idx1]] == 1: continue
    # 둘 다 0인데 3개 이상 있는 경우
    if seq[idx1] == 0 and seq[idx2] == 0:
        if dict[0] <= 2: continue
    res_set.add(seq[idx1]+seq[idx2])
answer = 0
for s in seq:
    if s in res_set: answer += 1

print(answer)