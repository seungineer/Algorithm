TC = int(input())
for _ in range(TC):
    seq = list(map(str, input()))
    isPossible = [True]

    def check(center, length):
        l = center - length
        r = center + length
        
        while l < r:
            if seq[l] != seq[r]:
                l += 1
                r -= 1
            else:
                isPossible[0] = False
                break
    
        if isPossible[0]:
            if length// 2 != 0:
                check(center + length//2 + 1, length//2)
                check(center - length//2 - 1, length//2)
    
    check(len(seq)//2,len(seq)//2)
    
    if isPossible[0]: print("YES")
    else: print("NO")