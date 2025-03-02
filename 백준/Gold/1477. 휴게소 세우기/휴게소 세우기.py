def solution():
    n, M, L = map(int, input().split())
    if n != 0:
        stations = [0] + list(map(int, input().split()))
    else:
        stations = [0]
    stations.append(L)
    stations.sort()
    n += 2

    def needStations(target):
        cnt = 0
        for i in range(1, n):
            diff = stations[i] - stations[i-1]
            cnt += (diff - 1) // target
        return cnt
    
    ans = L + 1
    l = 1
    r = L
    while l <= r:
        mid = (l + r) // 2
        # mid가 구간 길이의 최댓값일 때, 몇 개의 정류장을 더 설치해야 하는지?
        cnt = needStations(mid)
        if cnt <= M:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
        
    print(ans)
solution()