def solution():
    stk1 = list(map(str,input()))
    stk2 = []
    M = int(input())
    for _ in range(M):
        command = input()
        if len(command) > 1:
            command, character = map(str, command.split())
        if command == 'L':
            if len(stk1):
                stk2.append(stk1.pop())
            continue
        if command == 'D':
            if len(stk2):
                stk1.append(stk2.pop())
            continue
        if command == 'B':
            if stk1: stk1.pop()
            continue
        if command == 'P':
            stk1.append(character)
            continue
    print(''.join(stk1) + ''.join(stk2[::-1]))
    
solution()