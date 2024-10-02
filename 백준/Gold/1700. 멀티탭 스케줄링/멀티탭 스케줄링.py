from collections import deque
N, K = map(int, input().split())
seq = list(map(int, input().split()))
max_num = max(seq)
freq_lst = [deque() for _ in range(max_num + 1)]
for i in range(len(seq)):
    freq_lst[seq[i]].append(i)
tab_lst = set()
st = 0
while len(tab_lst) < N and st < len(seq):
    num = seq[st]
    if not num in tab_lst: tab_lst.add(num)
    freq_lst[num].popleft()
    st += 1
ans = 0
for i in range(st, len(seq)):
    num = seq[i]
    if num in tab_lst:
        if freq_lst[num]: freq_lst[num].popleft()
        continue
    else:
        # 탭 내 있는 숫자 중에서 가장 큰 수 tab_lst에서 제거
        max_ocurr_num = -1e9
        for tab_num in list(tab_lst):
            if len(freq_lst[tab_num]) != 0:
                if max_ocurr_num < freq_lst[tab_num][0]:
                    max_ocurr_num = freq_lst[tab_num][0]
                    longest_ocurr_num = tab_num
            else:
                # 더이상 등장하지 않는 것
                longest_ocurr_num = tab_num
                break
        # 탭 내 숫자 제거 및 새로운 숫자 add
        if freq_lst[num]: freq_lst[num].popleft()
        tab_lst.discard(longest_ocurr_num)
        tab_lst.add(num)
        ans += 1
    # print(num, tab_lst)
            
print(ans)