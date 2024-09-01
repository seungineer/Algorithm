N = int(input())
values = list(map(int, input().split()))
values.sort()
res = [0, 0, 0]
zero = float('inf')
for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        threeSum = values[i] + values[left] + values[right]
        if abs(threeSum) < zero:
            zero = abs(threeSum)
            res[0], res[1], res[2] = values[i], values[left], values[right]
        if threeSum > 0:
            right -= 1
        else:
            left += 1
print(*res)