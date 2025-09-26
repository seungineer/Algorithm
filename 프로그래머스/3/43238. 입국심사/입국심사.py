def solution(n, times):
    maxTime = max(times)
    maxWait = maxTime * n
    
    l = 1
    r = maxWait
    answer = maxWait
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
        
        if cnt < n:
            l = mid + 1
        else:
            answer = min(answer, mid)
            r = mid - 1

    return answer