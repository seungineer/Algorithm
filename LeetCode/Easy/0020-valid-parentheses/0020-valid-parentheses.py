class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        s = list(s)
        for i in range(1, len(s)+1):
            if s[-i] == ')' or s[-i] =='}' or s[-i] ==']':
                stk.append(s[-i])
            else:
                if len(stk) == 0:
                    return False
                if s[-i] == '(':
                    if stk[-1] != ')':
                        return False
                    stk.pop()
                elif s[-i] == '{':
                    if stk[-1] != '}':
                        return False
                    stk.pop()
                elif s[-i] == '[':
                    if stk[-1] != ']':
                        return False
                    stk.pop()
        if len(stk) != 0:
            return False
        return True