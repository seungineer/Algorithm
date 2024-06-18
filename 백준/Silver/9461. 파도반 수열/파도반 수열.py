arr = [0 for _ in range(101)]
arr[0] = 0
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2
for i in range(6, 101):
    arr[i] = arr[i-1] + arr[i-5]

n = int(input())
for _ in range(n):
    res = int(input())
    print(arr[res])