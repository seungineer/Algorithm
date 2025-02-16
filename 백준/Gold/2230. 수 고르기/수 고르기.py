from bisect import bisect_left
def solution():
    N, M = map(int, input().split())
    seq = [int(input()) for _ in range(N)]
    seq.sort()
    ans = int(1e10)
    for st in range(N):
        diff = M + seq[st]
        l = 0
        r = N-1
        while l <= r:
            mid = (l+r)//2
            if seq[mid] >= diff:
                if abs(seq[mid] - seq[st]) >= M:
                    ans = min(ans, abs(seq[mid] - seq[st]))
                r = mid - 1
            else:
                if abs(seq[mid] - seq[st]) >= M:
                    ans = min(ans, abs(seq[mid] - seq[st]))
                l = mid + 1
    
    print(ans)
    return
solution()