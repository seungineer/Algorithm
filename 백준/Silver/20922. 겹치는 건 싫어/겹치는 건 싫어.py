N, K = map(int, input().split())
seq = list(map(int, input().split()))
l = 0
cnt_dict = dict()
if seq[l] in cnt_dict: cnt_dict[seq[l]] += 1
else: cnt_dict[seq[l]] = 1

max_length = 1
for r in range(1, N):
    if seq[r] in cnt_dict: cnt_dict[seq[r]] += 1
    else: cnt_dict[seq[r]] = 1

    while cnt_dict[seq[r]] > K:
        cnt_dict[seq[l]] -= 1
        l += 1
    max_length = max(max_length, r - l + 1)
    
print(max_length)