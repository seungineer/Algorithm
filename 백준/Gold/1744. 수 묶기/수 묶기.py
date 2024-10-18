# 내림차순 정렬
# 0 인덱스부터 출발
# 양수부(내림차순 정렬)
## 양수인 경우
### 인덱스 + 1과 곱했을 때 자기 자신보다 더 큰 경우 인덱스 두 개 늘리기 반영
### 아닌 경우 플러스로 반영하고 인덱스 하나 늘리기
# 음수부(오름차순 정렬)
## 음수인 경우
### 인덱스 + 1과 곱했을 때 자기 자신보다 더 큰 경우 인덱스 두 개 늘리기 반영
### 아닌 경우 플러스로 반영하고 인덱스 하나 늘리기

N = int(input())
plus_lst = []
minus_lst = []
for _ in range(N):
    el = int(input())
    if el > 0: plus_lst.append(el)
    else: minus_lst.append(el)
plus_lst.sort(reverse=True)
minus_lst.sort()

answer = 0
idx = 0
while idx < len(plus_lst):
    if idx + 1 < len(plus_lst):
        if plus_lst[idx] * plus_lst[idx + 1] > plus_lst[idx]:
            answer += plus_lst[idx] * plus_lst[idx + 1]
            idx += 2
        else:
            answer += plus_lst[idx]
            idx += 1
    else:
        answer += plus_lst[idx]
        idx += 1

idx = 0
while idx < len(minus_lst):
    if idx + 1 < len(minus_lst):
        if minus_lst[idx] * minus_lst[idx + 1] > minus_lst[idx]:
            answer += minus_lst[idx] * minus_lst[idx + 1]
            idx += 2
        else:
            answer += minus_lst[idx]
            idx += 1
    else:
        answer += minus_lst[idx]
        idx += 1
print(answer)
