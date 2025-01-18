def solution():
    N = int(input())
    times = []
    points = []
    for _ in range(N):
        t, p = map(int, input().split())
        times.append(t)
        points.append(p)
    dp = [0 for _ in range(N+50)]
    for day in range(N):
        t, p = times[day], points[day]
        if not day == 0: dp[day] = max(dp[day], dp[day-1])
        dp[day+t] = max(dp[day+t], dp[day] + p)
    print(max(dp[:N+1]))

solution()
