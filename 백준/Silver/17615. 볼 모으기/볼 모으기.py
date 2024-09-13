N = int(input())
seq = list(map(str, input()))
rev_mov_r = 0
mov_r = 0
rev_mov_b = 0
mov_b = 0

rev_findB = False
findB = False
rev_findR = False
findR = False

for i in range(N-1, -1, -1):
    rev_s_r = seq[i]
    s_r = seq[N-1-i]

    if rev_findB:
        if rev_s_r == 'R':
            rev_mov_r += 1
            
    if rev_findR:
        if rev_s_r == 'B':
            rev_mov_b += 1
    
    if findB:
        if s_r == 'R':
            mov_r += 1
            
    if findR:
        if s_r == 'B':
            mov_b += 1
            
    if rev_s_r == 'R':
        rev_findR = True
    else:
        rev_findB = True
    
    if s_r == 'R':
        findR = True
    else:
        findB = True

print(min(rev_mov_r, rev_mov_b, mov_r, mov_b))