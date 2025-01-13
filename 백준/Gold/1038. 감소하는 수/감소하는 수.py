def solution():
    N = int(input())
    seq = [0]
    
    def bt(left, num):
        if left == 0:
            seq.append(num)
            return
        
        for i in range(int(str(num)[-1])):
            number = str(num)
            number += str(i)
            bt(left - 1, int(number))
    
    def make(length):
        for i in range(1, 10): # 맨 앞자리
            number = str(i)
            bt(length - 1, int(number))
    
    for length in range(1, 11):
        make(length)
    
    if N < len(seq): print(seq[N])
    else: print(-1)
    return 
solution()