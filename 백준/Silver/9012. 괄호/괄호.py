n = int(input())

data = [input().strip() for _ in range(n)]
a = []
flag = True

for str in data:
    for i in str:
        if i == '(':
            a.append(1)
        elif i == ')':
            if len(a) == 0:
                print('NO')
                flag = False
                break
            else:
                a.pop()
    if flag :
        if len(a) == 0:
            print('YES')
        else:
            print('NO')
    a.clear()
    flag = True