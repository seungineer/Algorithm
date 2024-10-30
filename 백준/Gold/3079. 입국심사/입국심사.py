# min(Tk)일 때, mid 시간 동안 몇명 처리 가능한지? -> x명이다. 하면
# 다음 반복 때 그다음 Tk일 때 mid 동안 몇명 처리? -> y명이다.
# ...
# x + y + z .... > M 이면, 더 많은 사람을 수용하는 시간이므로 r = mid - 1
# M보다 작으면, 더 적은 사람을 수용하는 시간 l = mid +  1

N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
max_t, min_t = T[-1], T[0]

def needMore(target):
    cnt = 0
    for Tk in T:
        cnt += target//Tk
        if cnt >= M: return False
    return True

r = int(1e19)
l = 0
min_target = int(1e19)
while l <= r:
    target = (l + r) // 2
    if needMore(target):
        l = target + 1
    else:
        min_target = min(min_target, target)
        r = target - 1
print(min_target)