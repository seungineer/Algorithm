n = int(input())
array = list(map(int, input().split()))
def factorial(inp):
    if inp <= 1:
        return 1
    else:
        return inp * factorial(inp - 1)
if array[0] == 1:
    k = array[1]
    nums = list(range(1, n + 1))
    temp = []
    for i in range(n, 0, -1):
        fac = factorial(i - 1)
        step = (k-1) // (fac)
        temp.append(nums[step])
        del nums[step]
        k -= fac * step
    print(*temp)

else:
    li = array[1:]
    nums = list(range(1, n + 1))
    k = 1
    for i in range(n, 0, -1):
        fac = factorial(i - 1)
        step = nums.index(li[n-i])
        del nums[step]
        k += fac * step
    print(k)