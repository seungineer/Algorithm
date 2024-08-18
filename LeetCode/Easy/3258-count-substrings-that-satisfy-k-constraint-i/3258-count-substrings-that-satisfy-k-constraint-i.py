class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        total_cnt = (n*(n+1)//2)
        for length in range(2*k, n+1):
            for st in range(n-length+1):
                cnt1 = 0
                cnt0 = 0
                for i in range(st, st+length):
                    if s[i] == '1':
                        cnt1 += 1
                    else:
                        cnt0 += 1
                if cnt1 > k and cnt0 > k:
                    total_cnt -= 1
        return(total_cnt)