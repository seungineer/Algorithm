S = input()
T = input()

len_s = len(S)
len_t = len(T)

back_ptr = len_t - 1
front_ptr = 0
isFlipped = False
while len_s != (back_ptr-front_ptr + 1):
    if not isFlipped:
        if T[back_ptr] == 'A':
            back_ptr -= 1
        else:
            back_ptr -= 1
            isFlipped = not isFlipped
    else:
        if T[front_ptr] == 'A':
            front_ptr += 1
        else:
            front_ptr += 1
            isFlipped = not isFlipped
isFind = False
if isFlipped:
    for k in range(len_s):
        if S[k] != T[back_ptr - k]:
            print(0)
            isFind = True
            break
    if not isFind:
        print(1)
else:
    for k in range(len_s):
        if S[k] != T[front_ptr + k]:
            print(0)
            isFind = True
            break
    if not isFind:
        print(1)
