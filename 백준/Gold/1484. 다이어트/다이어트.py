def solution():
    G = int(input())
    prev = 1
    curr = 2
    ans = []
    while prev < curr:
        target = curr ** 2 - prev ** 2
        if target == G:
            ans.append(curr)
            prev += 1
            continue
        if target > G:
            prev += 1
        else:
            curr += 1
    if ans:
        for el in ans: print(el)
    else:
        print(-1)
solution()