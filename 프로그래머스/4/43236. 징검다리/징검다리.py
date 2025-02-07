def solution(distance, rocks, n):
    # 거리의 최솟값 중 가장 큰 값 찾기
    # 거리를 기준으로
    # 최소 그 거리가 유지되기 위해서 몇 개의 바위를 제거해야 하는지 검사
    # n보다 작으면 최소 거리가 늘어나야 하고,
    # n과 같거나 크면, 최소 거리가 줄어야 함
    answer = 1
    rocks.append(distance)
    rocks.sort()
    
    def countRemove(d):
        st = 0
        removeCnt = 0
        for i in range(len(rocks)):
            if rocks[i] - st >= d:
                st = rocks[i]
            else:
                removeCnt += 1
        return removeCnt
        
    l = 1
    r = distance
    while l <= r:
        maxDistance = (l + r) // 2
        removeCnt = countRemove(maxDistance)

        if removeCnt > n:
            r = maxDistance - 1
        else:
            l = maxDistance + 1
            answer = max(answer, maxDistance)      
        
    return answer