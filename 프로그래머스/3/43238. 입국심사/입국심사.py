def solution(n, times):
    answer = int(1e18)
    # 기다리는 사람 수보다 더 많이 검사 가능한 경우
    ## 시간 줄이기
    
    # 기다리는 사람 수보다 더 적게 검사 가능한 경우
    ## 시간 늘리기
    
    l = 1
    r = int(1e18)
    while l <= r:
        mid = (l + r) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t
        
        if cnt >= n:
            answer = min(answer, mid)
            r = mid - 1
        else:
            l = mid + 1
            
    
    return answer