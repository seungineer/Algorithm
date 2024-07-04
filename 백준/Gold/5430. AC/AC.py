t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    input_str = input()
    n_str = len(input_str)
    pop = 0
    popleft = 0
    if n_str == 2:
        arr = []
    else:
        arr = list(map(int, input_str[1:len(input_str)-1].split(',')))
    
    isEven = True # 기본은 짝수
    isFault = False
    for i in range(len(p)):
        if p[i] == 'R':
            if isEven:
                isEven = False
            else:
                isEven = True
        else:
            if isEven:
                popleft += 1
            else:
                pop += 1
            if pop + popleft > n:
                isFault = True
                break
    if isFault:
        print("error")
    else:
        if isEven:
            print('[', end='')
            for j in range(popleft, n-pop):
                if j == n-pop-1:
                    print(arr[j], end='')
                else:
                    print(arr[j], end=',')
            print(']')
        else:
            print('[', end='')
            for j in range(n-pop-1, popleft-1, -1):
                if j == popleft:
                    print(arr[j], end='')
                else:
                    print(arr[j], end=',')
            print(']')