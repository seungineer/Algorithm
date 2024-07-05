n = int(input()) # 223.6**2 = 50000

# 첫 째 자리로 성공
en = int(n**(0.5)) + 1
isFirst = False
isSecond = False
isThird = False
isOver = False
for i in range(en):
    if i**2 == n:
        isFirst = True

if not isFirst:
    for i in range(en):
        for j in range(i, en):
            if i**2 + j**2 == n:
                isSecond = True
                isOver = True
                break
            if i**2 + j**2 > n:
                break
        if isOver:
            isOver = False
            break
    if not isSecond:
        for i in range(en):
            for j in range(i, en):
                for k in range(j, en):
                    if i**2 + j**2 + k**2 > n:
                        break
                    if i**2 + j**2 + k**2 == n:
                        isThird = True
                        isOver = True
                        break
                if isOver:
                    break
            if isOver:
                isOver = False
                break
        if not isThird:
            print(4)
        else:
            print(3)
    else:
        print(2)
else:
    print(1)