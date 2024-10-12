# 가장 많은 고층 빌딩이 보이는 빌딩에서 보이는 개수
# N = 50
# 각 빌딩마다 입력되는 빌딩의 기울기가 더 큰 기울기만 입력되도록 해야할듯?
# 최악 시간 복잡도: O(N(N+1)/2)

N = int(input())
seq = list(map(int, input().split()))
max_descent_right = [-1e9 for _ in range(N)] # 처음에는 어떤 수도 입력될 수 있음
max_descent_left = [1e9 for _ in range(N)] # 처음에는 어떤 수도 입력될 수 있음
cnt_lst = [0 for _ in range(N)]
for i in range(N): # 기준이 되는 인덱스
    # i 보다 오른쪽
    for j in range(i+1, N):
        if max_descent_right[i] < (seq[j] - seq[i]) / (j - i):
            max_descent_right[i] = ((seq[j] - seq[i]) / (j - i))
            cnt_lst[i] += 1
    # i 보다 왼쪽
    for j in range(i-1, -1, -1):
        if max_descent_left[i] > (seq[i] - seq[j]) / (i - j):
            max_descent_left[i] = ((seq[i] - seq[j]) / (i - j))
            cnt_lst[i] += 1

print(max(cnt_lst))