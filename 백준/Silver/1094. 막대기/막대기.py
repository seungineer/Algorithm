def solution():
    X = int(input())
    ans = 0
    while X != 0:
        if X % 2 == 1:
            ans += 1
        X //= 2

    print(ans)
    return
solution()