from collections import deque
N, K = map(int, input().split())
resources = list(map(int, input().split()))

step = 0
rotate = 0
robots = deque()
vis = [0 for _ in range(N)]
while True:
    if robots:
        # 벨트회전 로봇 상태 다루기
        isOut = False
        for i in range(len(robots)):
            conv_num, idx = robots[i][0], robots[i][1]
            # 옆으로 한 칸씩 무조건 밀기
            vis[idx] = 0
            vis[idx+1] = 1
            robots[i][1] += 1
            if idx + 1 == N-1:
                isOut = True
                vis[idx+1] = 0
                continue
        if isOut:
            robots.popleft()

        isOut = False
        for i in range(len(robots)):
            conv_num, idx = robots[i][0], robots[i][1]    
            if vis[idx + 1] == 0 and resources[(conv_num + 1)%(2*N)] >= 1:
                vis[idx] = 0
                vis[idx + 1] = 1
                robots[i][0] += 1
                if robots[i][0] == 2*N: robots[i][0] = 0 
                robots[i][1] += 1
                resources[(conv_num + 1)%(2*N)] -= 1
                if idx + 1 == N-1:
                    isOut = True
                    vis[idx + 1] = 0
        if isOut:
            robots.popleft()
    # 로봇 올리기
    # 초기 로봇 올리는 위치 유의....
    if rotate % (N*2) == 0: st = 2*N - 1
    else: st -= 1
    rotate += 1
    if resources[st] >= 1:
        resources[st] -= 1
        robots.append([st, 0]) # [컨베이어번호, 위치]
    step += 1

    if resources.count(0) >= K: break

print(step)