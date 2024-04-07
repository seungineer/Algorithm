import sys
input = sys.stdin.readline

k, n = map(int, input().split())
wlan_list = [int(input()) for _ in range(k)]

high = max(wlan_list)
low = 1
mid = (high + low) // 2
res_lst = []
while True:
    total = 0

    for element in wlan_list:
        total += element//mid

    if total >= n: # 잘게 쪼겠다
        low = mid + 1
        mid = (high + low) // 2

    else: # 너무 크게 쪼겠다
        high = mid - 1
        mid = (high + low) // 2

    if low > high:
        print(mid)
        break