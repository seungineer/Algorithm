from collections import deque
def solution(s):
    answer = True
    stk = deque()
    for i in range(len(s)):
        character = s[i]
        if not stk:
            stk.append(character)
            continue
        if character == "(":
            stk.append(character)
        else:
            if stk[-1] == "(":
                stk.pop()
    if stk:
        return False
    

    return True