n, m = map(int, input().split())
name_dic = {}
res = []
res_cnt = 0
for _ in range(n):
    name = input().strip()
    name_dic[name] = 1
for _ in range(m):
    name = input().strip()
    if name in name_dic.keys():
        res_cnt += 1
        res.append(name)
print(res_cnt)
for temp in sorted(res):
    print(temp)