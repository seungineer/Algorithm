# K개의 곳에 M명 배치 가능 (M <=  K)
# 가장 가까운 심판의 거리가 최대(최대한 듬성듬성)
# 더 많은 심판을 세울 수 있는 최소 거리 -> 최소 거리 증가
# 더 적은 심판을 세울 수 있는 최소 거리 -> 최소 거리 감소

N, M, K = map(int, input().split())
seq = list(map(int, input().split()))

def refreeCount(gap):
    # 갭보다 작으면 깃발을 못 꽂고,
    # 갭보다 크거나 같으면 깃발을 꽂고
    # 50개 모든 곳에서 출발해서 K개 꽂을 수 있는 케이스에서 스탑
    # K개가 안 되면, 가장 많이 꽂을 수 있는 cnt
    
    refDiff = float("inf")
    refOrder = ''
    
    for st in range(K):
        # st 인덱스에는 무조건 깃발 꽂힘
        order = ''
        cnt = 1
        for _ in range(st): order += '0'
        order += '1'
        prev = st
        
        for i in range(st + 1, K):
            if cnt == M:
                order += '0'
                continue
            if seq[i] - seq[prev] >= gap:
                prev = i
                order += '1'
                cnt += 1
            else:
                order += '0'
        if abs(cnt - M) < refDiff:
            refDiff = abs(cnt - M)
            refCnt = cnt
            refOrder = order
    
    return refCnt, refOrder
        
l = 1
r = N
ans = set()
while l <= r:
    length = (l + r) // 2
    refCnt, refOrder = refreeCount(length)
    # print(length)
    # print(refCnt, refOrder)
    if refCnt > M:
        l = length + 1
    elif refCnt < M:
        r = length - 1
    else:
        ans = refOrder
        l = length + 1

print(ans)