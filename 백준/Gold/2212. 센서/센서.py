# 1 3 6 6 7 9
# 1 3 6 9
# 2와 3으로 구간 합 5 최소
N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor_lst = sorted(sensor)

diff_lst = []
for i in range(1, len(sensor_lst)):
    diff_lst.append(sensor_lst[i] - sensor_lst[i-1])
diff_lst.sort()
answer = 0

for i in range(N - K):
    answer += diff_lst[i]
print(answer)