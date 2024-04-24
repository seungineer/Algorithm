n, m = map(int, input().split())
arr = [0] * m
start = 1

def func(k):
    global start
    if k == m:
        print(*arr)
        return

    for i in range(start, n+1):
            arr[k] = i
            start = i
            func(k+1)

func(0)