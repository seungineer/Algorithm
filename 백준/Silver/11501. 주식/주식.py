import sys
read = sys.stdin.readline
t = int(read())
for _ in range(t):
    n = int(read())
    price_lst = list(map(int, input().split()))
    high = 0
    profit = 0
    for i in range(len(price_lst)-1, -1, -1): # price_lst idx 고려한 범위
        if i == len(price_lst)-1: # 마지막 주가의 경우 항상 high
            high = price_lst[i]
        else: # 마지막 이외 주가 처리
            if high > price_lst[i]: # 가장 마지막 high보다 저렴한 경우 무조건 profit
                profit += high - price_lst[i]
            else: # 최근 high 보다 더 높은 price의 경우 high 갱신하기
                high = price_lst[i]
    print(profit)