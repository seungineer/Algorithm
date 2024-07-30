import itertools
n, m = map(int, input().split())
matrix = []
house_cnt = 0
house_x = []
house_y = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            house_cnt += 1
            house_x.append(i)
            house_y.append(j)

house = [[] for _ in range(house_cnt)]
chicken_cnt = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            chicken_cnt += 1
            for num in range(house_cnt):
                loc_x = house_x[num]
                loc_y = house_y[num]
                dist = abs(loc_x - i) + abs(loc_y - j)
                house[num].append(dist)
min_dist = float("inf")
cand_lst = list(itertools.combinations(range(chicken_cnt),m))
for k in cand_lst:
    dist = 0
    for h in house:
        min_length = float("inf")
        for el in k:
            min_length = min(min_length, h[el])
        dist += min_length
    min_dist = min(min_dist, dist)

print(min_dist)