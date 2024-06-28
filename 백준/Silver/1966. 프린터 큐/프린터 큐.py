t = int(input())
for _ in range(t):
    num, target_idx = map(int, input().split())
    lst = list(enumerate(list(map(int,input().split()))))
    
    cnt = 1
    while True:
        max_imp = max(i[1] for i in lst)
        if lst[0][1] >= max_imp:
            if lst[0][0] == target_idx:
                print(cnt)
                break
            else:
                lst.pop(0)
                cnt += 1
        else:
            lst.append(lst.pop(0))
        
