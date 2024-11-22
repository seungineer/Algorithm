# 양수부, 음수부 둘 다 존재하는 경우 어디에서 종료될 건지 정해야 됨
# 양수부에서 총 몇 번을 왔다갔다 해야하는지?
# 음수부에서 총 몇 번을 왔다갔다 해야하는지?
# 끝날 때, 안 끝날 때 각각 계산
## 양수부 끝날 때 값 + 음수부 안 끝날 때 값
## 음수부 끝날 때 값 + 양수부 안 끝날 때 값

N, M = map(int, input().split())
tasks = list(map(int, input().split()))
tasks.sort()

left_tasks = [0]
right_tasks = [0]
for t in tasks:
    if t < 0: left_tasks.append(-t)
    if t > 0: right_tasks.append(t)

left_tasks.sort()
right_tasks.sort()
answer = [0,0,0,0]

if left_tasks:
    left_tasks_set = [1 for _ in range(len(left_tasks))]
    for i in range(len(left_tasks)-1, -1, -M):
        setCnt = i
        if setCnt >= M: setCnt = M
        for j in range(i, i-M, -1):
            if j <= 0: continue
            left_tasks_set[j] = setCnt

    standard = 1
    acc = 0

    while standard != len(left_tasks):
        if standard + left_tasks_set[standard] == len(left_tasks):
            answer[0] = acc + left_tasks[-1]
            answer[1] = acc + (2 * left_tasks[-1])
        else:
            acc += 2* left_tasks[standard + left_tasks_set[standard] - 1]
        standard += left_tasks_set[standard]

right_tasks_set = [1 for _ in range(len(right_tasks))]
if right_tasks:
    right_tasks_set = [1 for _ in range(len(right_tasks))]
    for i in range(len(right_tasks)-1, -1, -M):
        setCnt = i
        if setCnt >= M: setCnt = M
        for j in range(i, i-M, -1):
            if j <= 0: continue
            right_tasks_set[j] = setCnt

    standard = 1
    acc = 0
    while standard != len(right_tasks):
        if standard + right_tasks_set[standard] == len(right_tasks):
            answer[2] = acc + right_tasks[-1]
            answer[3] = acc + (2 * right_tasks[-1])
        else:
            acc += 2* right_tasks[standard + right_tasks_set[standard] - 1]
        standard += right_tasks_set[standard]
print(min([answer[0] + answer[3], answer[1] + answer[2]]))