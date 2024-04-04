import heapq
n, k = map(int, input().split())
jewerly_list = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewerly_list, [m, -v])

bag_list = []
for _ in range(k):
    max_bag = int(input())
    bag_list.append(max_bag)

bag_list.sort(key=lambda x:(x)) # 허용 무게 작은 순

point = 0
j = len(jewerly_list)
possible_list = []
result = 0

for bag in bag_list:
    while len(jewerly_list) != 0:
        if bag >= jewerly_list[0][0]:
            heapq.heappush(possible_list, heapq.heappop(jewerly_list)[1])
            if len(jewerly_list) == 0:
                break
        else:
            break
    if len(possible_list)!= 0:
        result -= heapq.heappop(possible_list)
print(result)