import sys
sys.setrecursionlimit(10**6)
N = int(input())

def isPrime(checkNumber):
    for i in range(2, int(checkNumber**(0.5) + 1)):
        if checkNumber % i == 0: return False
    
    return True

def bt(number):
    if len(str(number)) == N:
        print(number)
        return
    
    for i in range(1, 10):
        
        next_cand = number * 10 + i
        if isPrime(next_cand):
            bt(next_cand)

for pos in range(9):
    if pos in [2, 3, 5, 7]:
        bt(pos)