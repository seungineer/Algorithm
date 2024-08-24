string = input()
answer = ''
isTag = False
stk = []
for s in string:
    if s == '<':
        answer += str(''.join(stk[::-1]))
        stk = []
        isTag = True
        answer += s
        continue
    if s == '>':
        isTag = False
        answer += s
        continue

    if isTag:
        answer += s
    else:
        if s == ' ':
            answer += str(''.join(stk[::-1]))
            stk = []
            answer += s
        else:
            stk.append(s)
if stk:
    answer += ''.join(stk[::-1])
print(answer)