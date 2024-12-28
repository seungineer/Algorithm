# L1
x1, y1, x2, y2 = map(int, input().split())
# L2
x3, y3, x4, y4 = map(int, input().split())

def f(xa, ya, xb, yb, x_input, y_input):
    return (yb - ya) * (x_input - xa) + ya * (xb - xa) + (xa - xb) * (y_input)

res1 = f(x1, y1, x2, y2, x3, y3)
res2 = f(x1, y1, x2, y2, x4, y4)

res3 = f(x3, y3, x4, y4, x1, y1)
res4 = f(x3, y3, x4, y4, x2, y2)

if (res1 == 0 and res2 == 0) or (res3 == 0 and res4 == 0):
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    
    if x3 > x4: x3, x4 = x4, x3
    if y3 > y4: y3, y4 = y4, y3

    if x2 < x3 or y2 < y3: # x1, x2 < x3, x4인 case
        print(0)
        exit()
    if x4 < x1 or y4 < y1: # x3, x4 < x1, x2인 case
        print(0)
        exit()
    
    print(1)
elif res1 * res2 <= 0 and res3 * res4 <= 0: print(1)
else: print(0)
