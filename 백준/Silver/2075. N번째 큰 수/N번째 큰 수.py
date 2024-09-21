N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
i_idx = [N-1 for _ in range(N)]
cnt = 0
while True:
    max_val = -float("inf")
    for j in range(N):
        i = i_idx[j]
        if max_val < matrix[i][j]:
            max_val = matrix[i][j]
            rec_j = j
    i_idx[rec_j] -= 1
    cnt += 1
    if cnt == N:
        answer = max_val
        print(answer)
        break