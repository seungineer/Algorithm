N, M = map(int, input().split())
total_weight = dict()
prices = set()
each_weight = dict()
for _ in range(N):
    weight, price = map(int, input().split())
    if price in total_weight: total_weight[price] += weight
    else: total_weight[price] = weight
    
    if price in each_weight: each_weight[price].append(weight)
    else: each_weight[price] = [weight]
    prices.add(price)

prices_lst = sorted(list(prices))
sum_w = 0
prev_sum_w = 0
min_ans = float("inf")
for price in prices_lst:
    sum_w += total_weight[price]
    if sum_w >= M:
        # 이전 단계부터 현재 price가 몇 번 필요한지 계산
        ans = 0
        p_weights = sorted(each_weight[price], reverse= True)
        # print(price, p_weights, prev_sum_w)
        for i in range(len(p_weights)):
            prev_sum_w += p_weights[i]
            if prev_sum_w >= M:
                min_ans = min(min_ans, (price * (i+1)))
    prev_sum_w = sum_w
if min_ans == float("inf"): print(-1)
else: print(min_ans)
