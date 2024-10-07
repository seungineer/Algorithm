N = int(input())

def find(k, prev_lst):
    new_lst = [0, 0, 0]
    for i in range(3):
        p = prev_lst[i]
        if i == 1:
            new_lst[i-1] += p
            new_lst[i+1] += p
            continue
        new_lst[1] += p
    k -= 1
    if k == 0:
        max_prob = -1
        for i in range(3):
            if max_prob < new_lst[i]:
                max_idx = i
                max_prob = new_lst[i]
        return max_idx
    res = find(k, new_lst)
    return res


for tc in range(1, N+1):
    # 초기상태, k
    init, K = input().split(" ")
    K = int(K)
    prob_lst = [0,0,0]
    for i in range(len(init)):
        if init[i] == 'o': prob_lst[i] = 1
    if K == 0:
        max_prob = -1
        for i in range(3):
            if max_prob < prob_lst[i]:
                max_idx = i
                max_prob = prob_lst[i]
        print(f"#{tc} {max_idx}")
        continue
    print(f"#{tc} {find(K, prob_lst)}")
