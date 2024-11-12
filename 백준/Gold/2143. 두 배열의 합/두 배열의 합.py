# 어짜피 개수만 구하면 되니까
# A의 부분으로 x를 만들 수 있다 / B의 부분으로 y를 만들 수 있다
# x가 땡땡이면 y는 T - x로 고정된다.
# A 정렬 후에 누적합 / B 정렬 후에 누적합
# T를 만들어야 하니까, A가 몇일 때, B가 몇이어야 한다.

# A가 몇인 경우의 수를 좍 센 다음에
# A가 몇일 때, B가 몇인지 곱해서 토탈 구하면 될 거 같다.

T = int(input())
N = int(input())
lst_a = list(map(int, input().split()))
M = int(input())
lst_b = list(map(int, input().split()))

def find(acc, idx, lst, part_sum):
    if idx == len(lst): return
    acc += lst[idx]
    if acc in part_sum.keys(): part_sum[acc] += 1
    else: part_sum[acc] = 1

    find(acc, idx+1, lst, part_sum)

part_sum_a = dict()
for i in range(N):
    find(0, i, lst_a, part_sum_a)
part_sum_b = dict()
for i in range(M):
    find(0, i, lst_b, part_sum_b)
answer = 0
for key_a in part_sum_a.keys():
    target = T - key_a
    if target in part_sum_b.keys():
        cnt_b = part_sum_b[target]
    else: continue
    cnt_a = part_sum_a[key_a]
    answer += (cnt_a * cnt_b)

print(answer)