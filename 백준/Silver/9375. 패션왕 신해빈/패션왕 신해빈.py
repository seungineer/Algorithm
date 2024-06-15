iterate_time = int(input())
for _ in  range(iterate_time):
    clothes = {}
    n = int(input())
    for i in range(n):
        name, type = input().split()
        if type in clothes.keys():
            clothes[type] += 1
        else:
            clothes[type] = 1    
    cnt = 1
    clothes_lst = list(clothes)
    for k in clothes_lst:
        cnt *= (clothes[k]+1)
    print(cnt - 1)