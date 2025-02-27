N, P, Q = map(int, input().split())
if P < Q:
    P, Q = Q, P

def divide(i):
    if i == 0:
        return 1
    if i in res:
        return res[i]
    
    res[i] = divide(i//P) + divide(i//Q)
    return res[i]

res = dict()
print(divide(N))