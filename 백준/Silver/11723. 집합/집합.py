import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    S = 0b0
    for _ in range(N):
        inputs = input().rstrip().split()
        if len(inputs) == 2:
            command, num = inputs[0], int(inputs[1])
        else:
            command = inputs[0]
        if command == 'all':
            S = 0b111111111111111111111
        if command == 'add':
            S = S | (0b1 << num)
        if command == 'check':
            if S & (0b1 << num) : print(1)
            else: print(0)
        if command == 'remove':
            if S & 0b1 << num:
                S = S ^ (0b1 << num)
        if command == 'toggle':
            if S & 0b1 << num:
                S = S ^ (0b1 << num)
            else:
                S = S | (0b1 << num)
        if command == 'empty':
            S = 0b0

        
solution()