# 강의길이 최대 값을 l
# 강의 길이 최대 값 * 개수를 r로 잡고
# M개에 나뉘어 담아 지는지 체크
## M개가 모자라면 l = mid + 1
## M개가 남으면 r = mid - 1
N, M = map(int, input().split())
seq = list(map(int, input().split()))
l = max(seq)
r = l * N
mid = (l+r)//2
answer = 1e9
while l <= r:
    size = mid
    cnt = 0
    for s in seq:
        if size - s > 0:
            size -= s
        elif size - s == 0:
            cnt += 1
            size = mid
        else:
            cnt += 1
            size = mid - s
    if size != mid: cnt += 1
    if cnt > M:
        l = mid + 1
    else:
        answer = min(answer, mid)
        r = mid - 1
    mid = (l+r)//2

print(answer)