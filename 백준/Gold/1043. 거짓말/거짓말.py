N, M = map(int, input().split())
truth_group_str = input()
truth_group = set()
if truth_group_str[0] != '0':
    truth_group_str = truth_group_str[1:]
    for k in list(map(int, truth_group_str.split())):
        truth_group.add(k) # {1, 2, 3, 4}
party_lst = []
if len(truth_group) == 0:
    for _ in range(M):
        temp = list(map(int, input().split()))
    print(M)
else:
    for _ in range(M):
        party_lst.append(list(map(int,input().split())))

    isUpdate = True
    while isUpdate:
        res = 0
        truth_group_cnt = len(truth_group)
        for party in party_lst:
            isIn = False
            for i in range(1, party[0]+1):
                if party[i] in truth_group:
                    isIn = True
            if isIn:
                for i in range(1, party[0]+1):
                    truth_group.add(party[i])
            else:
                res += 1
        if truth_group_cnt == len(truth_group):
            isUpdate = False
    print(res)