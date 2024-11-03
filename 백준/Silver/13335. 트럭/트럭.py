from collections import deque
N, W, L = map(int, input().split())
seq = deque(map(int, input().split()))

ans = 1
bridge = deque()
truck = seq.popleft()
weight = L - truck
bridge.append([truck, 1])
ans = 1
while bridge:
    ans += 1
    isOver = False
    # print(seq, bridge)
    for i in range(len(bridge)):
        bridge[i][1] += 1
        if bridge[i][1] == W + 1:
            weight += bridge[i][0]
            isOver = True
    if isOver: bridge.popleft()
    # print(ans, weight)
    if seq and weight >= seq[0]:
        truck_weight = seq.popleft()
        bridge.append([truck_weight, 1])
        weight -= truck_weight
print(ans)