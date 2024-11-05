tc = int(input())
for _ in range(tc):
    N = int(input())
    lst = []
    for _ in range(N):
        input_nums = input()
        length_nums = len(input_nums)
        form_length = 10 - length_nums
        input_nums += ('0' * form_length)
        lst.append([input_nums, length_nums])
    lst.sort()
    if N == 1:
        print("YES")
        continue
    for i in range(N-1):
        target_nums = lst[i][0]
        end_idx = lst[i][1]
        isImpossible = False
        for j in range(end_idx):
            if lst[i+1][0][j] != target_nums[j]:
                isImpossible = True  
        if not isImpossible:
            print("NO")
            break
    if isImpossible: print("YES")