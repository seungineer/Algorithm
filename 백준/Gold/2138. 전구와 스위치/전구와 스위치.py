N = int(input())
seq = input()
target_seq = input()
dp = []
if seq[0] == target_seq[0]:
    dp = [[1, 0], [1, 0]]
else:
    dp = [[0, 1], [1, 0]]

for i in range(1, N-1):
    if seq[i] != target_seq[i]:
        tempA = dp[-1]
        tempB = dp[-2]
        dp.append([])
        for i in range(2):
            tot = tempA[i] + tempB[i]
            if tot % 2 == 0:
                dp[-1].append(1)
            else:
                dp[-1].append(0)
    else:
        tempA = dp[-1]
        tempB = dp[-2]
        dp.append([])
        for i in range(2):
            tot = tempA[i] + tempB[i]
            if tot % 2 == 0:
                dp[-1].append(0)
            else:
                dp[-1].append(1)

# 꽁다리 두 개 맞추기
isPrint = False
for i in range(2):
    tempA = dp[-1][i]
    tempB = dp[-2][i]
    tot = tempA + tempB
    if seq[-1] != target_seq[-1]:
        if tot % 2 != 0:
            # 최소 횟수 출력
            isPrint = True
    else:
        if tot % 2 == 0:
            isPrint = True
min_cnt = float("inf")
# print(dp)
if N == 2:
    if seq[-1] == seq[-2]:
        if target_seq[-1] == target_seq[-2]:
            isPrint = True
    else:
        if target_seq[-1] != target_seq[-2]:
            isPrint = True


if isPrint:
    left_cnt = 0
    right_cnt = 0
    for d in dp:
        left_cnt += d[0]
        right_cnt += d[1]
    
    if seq[-1] != target_seq[-1]:
        if (dp[-1][0] + dp[-2][0]) % 2 == 1:
            min_cnt = min(min_cnt, left_cnt)
        if (dp[-1][1] + dp[-2][1]) % 2 == 1:
            min_cnt = min(min_cnt, right_cnt)
    else:
        if (dp[-1][0] + dp[-2][0]) % 2 == 0:
            min_cnt = min(min_cnt, left_cnt)
        if (dp[-1][1] + dp[-2][1]) % 2 == 0:
            min_cnt = min(min_cnt, right_cnt)

    print(min_cnt)
else:
    print(-1)
