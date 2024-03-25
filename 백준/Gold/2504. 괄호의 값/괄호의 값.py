str = list(input())
temp = 1
stack = []
answer = 0
for i in range(len(str)):
    if str[i] == "(":
        stack.append(str[i])
        temp *= 2
    elif str[i] == "[":
        stack.append(str[i])
        temp *= 3
    elif str[i] == ")":
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if str[i-1] == "(":
            answer += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] =='(':
            answer = 0
            break
        if str[i-1] == "[":
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)


