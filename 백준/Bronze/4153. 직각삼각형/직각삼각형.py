while True:
    a, b, c = map(int, input().split())
    z = max(a, b, c)
    if z == a:
        a = c
    elif z == b:
        b = c

    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == z**2:
        print("right")
    else:
        print("wrong")