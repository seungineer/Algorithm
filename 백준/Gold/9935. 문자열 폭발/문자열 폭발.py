seq = str(input())
target = str(input())
stack = []

cnt = 0
for i in seq:
    stack.append(i)
    if len(target) <= len(stack) and stack[-1] == target[-1]:
        for i in range(1, len(target)+1):
            if stack[-i] == target[-i]:
                cnt += 1
        if cnt == len(target):
            cnt = 0
            for _ in range(len(target)):
                stack.pop()
        cnt = 0


if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
