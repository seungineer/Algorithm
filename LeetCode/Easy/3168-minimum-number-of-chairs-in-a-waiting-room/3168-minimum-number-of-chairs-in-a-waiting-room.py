class Solution:
    def minimumChairs(self, s: str) -> int:
        n = len(s)
        stk = []
        max_len = -1
        for i in range(n):
            if s[i] == "E":
                stk.append("E")
                max_len = max(max_len, len(stk))
            else:
                stk.pop()
        return max_len