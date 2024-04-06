n = int(input())
stack = []
result = []

i = 1    
flag = True
for _ in range(n):
    element = int(input())
    while True:
        if element >= i and i <= n+1:
            stack.append(i)
            result.append('+')
            i += 1
        elif element == stack[-1]:
            stack.pop()
            result.append('-')
            break
        else:
            flag = False
            break
    if flag == False:
        break

if len(stack)==0:
    for k in result:
        print(k)
else:
    print('NO')