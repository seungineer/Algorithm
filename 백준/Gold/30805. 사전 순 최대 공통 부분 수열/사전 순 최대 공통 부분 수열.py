N = int(input())
seq_a = list(map(int, input().split()))
M = int(input())
seq_b = list(map(int, input().split()))

st_a = 0
st_b = 0
answer = []
while True:
    common_big = [[0,-1,-1]]
    isStop = True
    max_number = 0
    for i in range(st_a, N):
        for j in range(st_b, M):
            if seq_a[i] == seq_b[j] and seq_a[i] > max_number:
                isStop = False
                if common_big[-1][0] == seq_a[i] and common_big[-1][2] < j:
                    common_big.append([seq_a[i], i, j])
                else: common_big = [[seq_a[i], i, j]]
                max_number = common_big[-1][0]

    st_a = common_big[-1][1] + 1
    st_b = common_big[-1][2] + 1
    if isStop: break
    
    answer.append(common_big)

temp = []
cnt = 0
if len(answer) != 0:
    for ans in answer:
        for a in ans:
            cnt += 1
            temp.append(a[0])
    print(cnt)
    print(*temp)
else:
    print(0)
