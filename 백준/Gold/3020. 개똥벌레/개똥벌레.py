# 번갈아가며 아래 위 아래 위 .... 반복
# 파괴 장애물의 최소 개수, 구간의 개수
# H는 완전 탐색 & N을 이진 탐색으로 찾음 5 * 10^5 * log(2*10^5)
up_lst = []
down_lst = []
N, H = map(int, input().split())
for i in range(N):
    if i % 2: up_lst.append(int(input()))
    else: down_lst.append(int(input()))
up_lst.sort()
down_lst.sort()

answer = 1e9
for height in range(1,H+1):
    # height랑 같은 것은 뿌시지 않음
    # height가 1이면 0~1 사이에서 나는 것 == 4~5사이에서 나는 것
    l = 0
    r = len(down_lst) - 1
    down_min_cnt = 0
    while l <= r:
        mid = (l+r)//2
        if down_lst[mid] >= height:
            down_min_cnt = max(down_min_cnt, len(down_lst) - mid)
            r = mid - 1
        else:
            l = mid + 1
    
    l = 0
    r = len(up_lst) - 1
    up_min_cnt = 0
    height = H - height + 1
    while l <= r:
        mid = (l+r)//2
        if up_lst[mid] >= height:
            up_min_cnt = max(up_min_cnt, len(up_lst) - mid)
            r = mid - 1
        else:
            l = mid + 1

    if answer > (up_min_cnt + down_min_cnt):
        answer = (up_min_cnt + down_min_cnt)
        answer_cnt = 1
    elif answer == (up_min_cnt + down_min_cnt):
        answer_cnt += 1
print(answer, answer_cnt)