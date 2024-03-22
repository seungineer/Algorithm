n, k = map(int, input().split())
str_num = input().strip()

#계속 append 해나가면서
## push 값과 비교했을 때 더 작으면 pop
## k 값 만큼 지웠으면 계속 append
stack = []

for i in range(len(str_num)):
    while(k > 0 and stack and int(stack[-1]) < int(str_num[i])): # 2 3 1 4 4
        # k가 허용하는 만큼 str_num[i] 보다 작은 stack의 top 녀석들은 .pop() 당함
        stack.pop()
        k -= 1
    stack.append(str_num[i])
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))