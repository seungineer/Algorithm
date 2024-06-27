while True:
    stk = []
    isErr = False
    string = list(input())
    if len(string)== 1 and string[0] == '.':
        break
    for k in string:
        if k == '(':
            stk.append(k)
        if k == '[':
            stk.append(k)        
        if k == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                isErr = True
                break
        if k == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                isErr = True
                break
    if len(stk)==0 and not isErr:
        print("yes")
    else:
        print("no")