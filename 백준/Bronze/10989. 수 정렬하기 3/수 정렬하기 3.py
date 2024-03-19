import sys

N = int(input())
# data = [int(read()) for _ in range(N)]

# 로직
lst = [0] * 10001 # 들어오는 수는 1 ~ 10000

for i in range(N):
    lst[int(input())] += 1

# lst에 1이상의 값이 있는 경우에만 출력하도록
## 

for i in range(len(lst)):
    if lst[i] !=0:
        for j in range(lst[i]):
            print(i)