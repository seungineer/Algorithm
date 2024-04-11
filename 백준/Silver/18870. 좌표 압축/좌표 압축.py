import sys
read = sys.stdin.readline

n = int(read())
seq = list(map(int, read().split()))
set_listed = list(set(seq))
set_listed_sorted = sorted(set_listed)

for k in seq:
    left = 0 # 시작 idx
    right = len(set_listed_sorted) - 1 # 마지막 idx
    while left < right:
        mid = (left + right)//2 # 중앙 idx
        if set_listed_sorted[mid] < k:
            left = mid + 1
            
        elif set_listed_sorted[mid] > k:
            right = mid - 1
            
        else: # 같을 때
            print(mid, end=' ')
            break
    if left >= right:
        print(right, end=' ')