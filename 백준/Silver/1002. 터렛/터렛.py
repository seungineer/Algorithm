T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 터렛 위치가 동일하고, r이 같은 경우 -> -1
    # 터렛 위치가 동일하고, r이 다른 경우 -> 0
    if r1 == r2:
        if x1 == x2 and y1 == y2:
            if r1 == r2: print(-1)
            else: print(0)
            continue    
        # 터렛 위치가 다른데, 두 터렛 간 거리가 r1 + r2와 같은 경우 -> 1
        # 터렛 위치가 다른데, 두 터렛 간 거리가 r1 + r2 보다 작은 경우 -> 2
        # 터렛 위치가 다른데, 두 터렛 간 거리가 r1 + r2 보다 큰 경우 -> 0
        distance_sqr = ((x1-x2)**2 + (y1-y2)**2)

        if distance_sqr > (r1 + r2)**2: print(0)
        elif distance_sqr < (r1 + r2)**2: print(2)
        else: print(1)
    else:
        if r2 < r1:
            t1, t2, t3 = x1, y1, r1
            x1, y1, r1 = x2, y2, r2
            x2, y2, r2 = t1, t2, t3
        # 무조건 r1 < r2임
        if x1 == x2 and y1 == y2:
            if r1 == r2: print(-1)
            else: print(0)
            continue
        distance_sqr = ((x1-x2)**2 + (y1-y2)**2)
        tot_r_sqr = (r1 + r2)**2
        if distance_sqr > tot_r_sqr: print(0)
        elif distance_sqr == tot_r_sqr: print(1)
        else:
            if distance_sqr == (r1 - r2)**2: print(1)
            elif distance_sqr < (r1 - r2)**2: print(0)
            else: print(2)
