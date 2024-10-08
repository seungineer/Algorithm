# 한 집에 한 공유기만 설치
# 최대한 많은 곳에서 왕이파이를 사용하기 위해,
# "가장 인접한 두 공유기 사이의 거리를 가능한 크게" 하여 설치
# TC: 2 * 10^5 * log(10^9)
# 최소 거리보다 큰 경우 설치 후 카운트
N, C = map(int, input().split())
house_lst = [int(input()) for _ in range(N)]
house_lst.sort()

l = 0
r = house_lst[-1] - house_lst[0]
min_diff = -1e9
while l <= r:
    mid = (l+r)//2
    prev_x = house_lst[0]
    cnt = 1
    for i in range(1, N):
        if house_lst[i] - prev_x >= mid:
            cnt += 1
            prev_x = house_lst[i]
    if cnt >= C:
        min_diff = max(min_diff, mid)
        l = mid + 1
    else:
        r = mid - 1
print(min_diff)
