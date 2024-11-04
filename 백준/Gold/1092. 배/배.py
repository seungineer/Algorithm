# 시간을 이진탐색으로 찾으면서
# 해당 시간 동안
# 처리 가능한지
## 가장 처리 용량 큰 녀석부터
## 시간 만큼 짐 처리
### 짐이 남으면 l = mid + 1
### 짐이 모자라면 r = mid - 1
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int,input().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)

l = 1
r = 10**4
min_time = 1e9
while l <= r:
    time = (l + r) // 2
    last_processed = 0
    cnt = 0
    for crane in cranes:
        work_load = time
        for i in range(last_processed, len(boxes)):
            if crane < boxes[i]: break
            if work_load == 0: break
            work_load -= 1
            cnt += 1
            last_processed += 1
    if cnt < len(boxes):
        l = time + 1
    else:
        r = time - 1
        min_time = min(min_time, time)
if min_time == 1e9: print(-1)
else: print(min_time)