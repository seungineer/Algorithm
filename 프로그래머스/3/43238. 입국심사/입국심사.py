def solution(n, times):
    answer = 1e9
    l = 1
    r = max(times) * n
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