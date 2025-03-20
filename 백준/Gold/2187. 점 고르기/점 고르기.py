def solution():
    N, A, B = map(int, input().split())
    candidates = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for st in range(N):
        st_x, st_y, st_s = candidates[st]
        for en in range(st+1, N):
            en_x, en_y, en_s = candidates[en]
            if abs(st_x - en_x) + 1 <= A and abs(st_y - en_y) + 1 <= B:
                ans = max(ans, abs(st_s - en_s))
    print(ans)

solution()