import sys

read = sys.stdin.readline
N = 9
data = [int(read()) for _ in range(N)]
total = sum(data)
flag = True
#로직
data.sort(reverse=True)
for i in range(8):
    for j in range(i+1, 9):
        if total - data[i] - data[j] == 100:
            data1, data2 = data[i], data[j]
            data.remove(data1)
            data.remove(data2)
            flag = False
            break
    if flag == False:
        break

data.sort()
for i in data:
    print(i)