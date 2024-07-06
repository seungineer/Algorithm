n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

arr = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            arr[i] += 1
print(*arr)