N = int(input())
lst = list(map(int, input().split()))
lst.sort()
l = 0
r = len(lst) - 1
min_diff = float("inf")
while l < r:
    mid = (lst[l]+lst[r])
    
    if min_diff > abs(mid):
        ans_l = l
        ans_r = r
        min_diff = abs(mid)
    
    if mid > 0: r -= 1
    elif mid < 0: l += 1
    else: break
print(lst[ans_l],lst[ans_r])
