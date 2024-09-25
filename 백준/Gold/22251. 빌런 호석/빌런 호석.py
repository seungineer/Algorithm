matrix = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]
N, K, P, X = map(int, input().split())
len_X = len(str(X))
if len_X < K: X_str = "0" * (K - len_X) + str(X)
else: X_str = str(X)
answer = 0

for target in range(1, N+1):
    # target_str 도출
    if len(str(target)) < K: target_str = "0" * (K - len(str(target))) + str(target)
    else: target_str = str(target)
    # X_str과 비교하여 P 범위내로 가능하면 answer += 1
    cnt = 0
    for i in range(K):
        if X_str[i] == target_str[i]: continue
        cnt += matrix[int(X_str[i])][int(target_str[i])]
    if 1<= cnt and cnt <= P: 
        answer += 1

print(answer)