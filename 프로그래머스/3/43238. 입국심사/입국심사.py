def solution(n, times):
    l = 1
    r = max(times) * n
    answer = r
    while l <= r:
        mid = (l+r)//2
        people_cnt = 0
        for time in times:
            people_cnt += mid//time
            if people_cnt >= n: break
        if people_cnt >= n:
            r = mid - 1
            answer = min(mid, answer)
        else:
            l = mid + 1
    return answer